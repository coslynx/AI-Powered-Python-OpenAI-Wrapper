from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    email: str = Field(..., example="user@example.com")
    password: str = Field(..., example="P@$$w0rd")

class User(BaseModel):
    id: int
    email: str
    is_active: bool
    api_key: str

class ApiKeyCreate(BaseModel):
    key: str = Field(..., example="YOUR_API_KEY")
    user_id: int = Field(..., example=1) 

class TextGenerationRequest(BaseModel):
    task: str = "generate_text" 
    input_text: str
    model: str = "text-davinci-003"
    temperature: float = 0.7

    @validator("temperature")
    def temperature_range(cls, value):
        if not 0 <= value <= 1:
            raise ValueError("Temperature must be between 0 and 1")
        return value

class TextGenerationResponse(BaseModel):
    choices: list[Choice]
    created: int
    model: str
    usage: Usage

class Choice(BaseModel):
    text: str
    index: int
    logprobs: Optional[str] = None
    finish_reason: str

class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int