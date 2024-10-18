from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from . import schemas, models
from database import get_db
import openai
import jwt

router = APIRouter(prefix="/api", tags=["API"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/generate_text")
async def generate_text(request: schemas.TextGenerationRequest, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user = db.query(models.User).filter(models.User.email == payload["sub"]).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        response = openai.Completion.create(
            engine=request.model,
            prompt=request.input_text,
            temperature=request.temperature,
            max_tokens=1024,  # Set a reasonable limit for token generation
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return response
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    except openai.error.APIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API Error: {e}")