from fastapi.testclient import TestClient
from main import app
from utils.auth_utils import create_access_token
from datetime import timedelta
import openai

client = TestClient(app)

# Test for successful text generation
def test_generate_text_success():
    response = client.post(
        "/api/generate_text",
        json={"input_text": "Write a short story about a robot who dreams.", "model": "text-davinci-003", "temperature": 0.7},
        headers={"Authorization": f"Bearer {create_access_token(data={'sub': 'testuser@example.com'})}"},
    )
    assert response.status_code == 200
    assert "choices" in response.json()
    assert response.json()["choices"][0]["text"] is not None

# Test for invalid token
def test_generate_text_invalid_token():
    response = client.post(
        "/api/generate_text",
        json={"input_text": "Write a short story about a robot who dreams.", "model": "text-davinci-003", "temperature": 0.7},
        headers={"Authorization": f"Bearer invalid-token"},
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid token"

# Test for expired token
def test_generate_text_expired_token():
    expired_token = create_access_token(data={'sub': 'testuser@example.com'}, expires_delta=timedelta(seconds=-1))
    response = client.post(
        "/api/generate_text",
        json={"input_text": "Write a short story about a robot who dreams.", "model": "text-davinci-003", "temperature": 0.7},
        headers={"Authorization": f"Bearer {expired_token}"},
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Token expired"

# Test for OpenAI API error
def test_generate_text_openai_error(monkeypatch):
    def mock_openai_error(*args, **kwargs):
        raise openai.error.APIError("Test API Error")

    monkeypatch.setattr(openai, "Completion", mock_openai_error)
    response = client.post(
        "/api/generate_text",
        json={"input_text": "Write a short story about a robot who dreams.", "model": "text-davinci-003", "temperature": 0.7},
        headers={"Authorization": f"Bearer {create_access_token(data={'sub': 'testuser@example.com'})}"},
    )
    assert response.status_code == 500
    assert "OpenAI API Error" in response.json()["detail"]

# Test for invalid request parameters
def test_generate_text_invalid_parameters():
    response = client.post(
        "/api/generate_text",
        json={"input_text": "Write a short story about a robot who dreams.", "model": "invalid-model", "temperature": 1.5},
        headers={"Authorization": f"Bearer {create_access_token(data={'sub': 'testuser@example.com'})}"},
    )
    assert response.status_code == 422  # Unprocessable Entity
    assert "value error" in response.json()["detail"][0]["msg"].lower()

# Test for successful user signup
def test_signup_success():
    response = client.post("/api/v1/auth/signup", json={"email": "newuser@example.com", "password": "securepass123"})
    assert response.status_code == 200
    assert response.json()["message"] == "User created successfully"

# Test for existing user signup
def test_signup_existing_user():
    response = client.post("/api/v1/auth/signup", json={"email": "testuser@example.com", "password": "securepass123"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"

# Test for successful user login
def test_login_success():
    response = client.post("/api/v1/auth/login", data={"username": "testuser@example.com", "password": "securepass123"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "token_type" in response.json()

# Test for invalid login credentials
def test_login_invalid_credentials():
    response = client.post("/api/v1/auth/login", data={"username": "testuser@example.com", "password": "wrongpassword"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password"