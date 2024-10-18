FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DATABASE_URL=${DATABASE_URL} \
    OPENAI_API_KEY=${OPENAI_API_KEY} \
    JWT_SECRET_KEY=${JWT_SECRET_KEY}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]