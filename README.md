<div class="hero-icon" align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</div>

<h1 align="center">
AI Powered Python Wrapper Service
</h1>
<h4 align="center">A robust backend service simplifying interactions with OpenAI's language models.</h4>
<h4 align="center">Developed with the software and tools below.</h4>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Framework-FastAPI-blue" alt="Framework used: FastAPI">
  <img src="https://img.shields.io/badge/Backend-Python-red" alt="Backend language: Python">
  <img src="https://img.shields.io/badge/Database-PostgreSQL-blue" alt="Database used: PostgreSQL">
  <img src="https://img.shields.io/badge/API-OpenAI-black" alt="API Integration: OpenAI">
</div>
<div class="badges" align="center">
  <img src="https://img.shields.io/github/last-commit/coslynx/AI-Powered-Python-OpenAI-Wrapper?style=flat-square&color=5D6D7E" alt="git-last-commit" />
  <img src="https://img.shields.io/github/commit-activity/m/coslynx/AI-Powered-Python-OpenAI-Wrapper?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
  <img src="https://img.shields.io/github/languages/top/coslynx/AI-Powered-Python-OpenAI-Wrapper?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

## 📑 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 Structure
- 💻 Installation
- 🏗️ Usage
- 🌐 Hosting
- 📄 License
- 👏 Authors

## 📍 Overview

The repository contains a Minimum Viable Product (MVP) called "AI Powered Python Wrapper Service" that provides a streamlined backend service for integrating OpenAI's powerful language models into applications. This service acts as an intermediary between developers and the OpenAI API, offering a user-friendly interface and abstracting away the complexities of direct API interactions. 

## 📦 Features

|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a clean and modular architecture, organized into distinct components for API routes, database models, and utility functions.   |
| 📄 | **Documentation**  | This README file provides a comprehensive overview of the MVP, its functionalities, dependencies, and usage instructions.        |
| 🔗 | **Dependencies**   | The project utilizes key libraries like FastAPI for building the RESTful API, OpenAI for interacting with AI models, SQLAlchemy for database operations, and JWT for authentication. |
| 🧩 | **Modularity**     | The codebase is structured into separate modules for routes, models, schemas, and utilities, promoting code reuse and maintainability. |
| 🧪 | **Testing**        |  Unit tests are implemented to ensure the correctness of individual functions and components.                                        |
| ⚡️  | **Performance**    | The service is designed to handle requests efficiently, optimizing API calls and minimizing response times.                      |
| 🔐 | **Security**       | Robust authentication and authorization mechanisms protect sensitive data and API keys.                               |
| 🔀 | **Version Control**| Utilizes Git for version control with a clear branching strategy to manage code changes and releases.                   |
| 🔌 | **Integrations**   |  Seamlessly integrates with the OpenAI API, leveraging its models for text generation, translation, and other capabilities.          |
| 📶 | **Scalability**    | The architecture is designed to handle increased user load and demands, utilizing cloud infrastructure and efficient resource management.        |

## 📂 Structure
```text
ai-wrapper-service/
├── api
│   └── routes
│       ├── auth.py
│       └── text.py
├── models.py
├── schemas.py
├── tests
│   └── test_routes.py
├── utils
│   └── auth_utils.py
├── .env
├── requirements.txt
├── main.py
├── README.md
└── .gitignore
```
      
## 💻 Installation
  ### 🔧 Prerequisites
  - Python 3.9+
  - PostgreSQL 13+
  - Docker 20.10+
  - `pip` package manager

  ### 🚀 Setup Instructions
  1. Clone the repository:
     ```bash
     git clone https://github.com/coslynx/AI-Powered-Python-OpenAI-Wrapper.git
     cd AI-Powered-Python-OpenAI-Wrapper
     ```
  2. Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
  3. Set up the database:
     - Create a database named `ai_wrapper_service` in PostgreSQL.
     - Update the `DATABASE_URL` environment variable in the `.env` file with the correct connection string.
     - Run the following command to create the database tables:
     ```bash
     python -m sqlalchemy.orm create -u "$DATABASE_URL"
     ```
  4. Configure environment variables:
     - Make a copy of the `.env.example` file:
     ```bash
     cp .env.example .env
     ```
     - Update the environment variables in the `.env` file with your OpenAI API key and database credentials.
     
 ## 🏗️ Usage
  ### 🏃‍♂️ Running the MVP
  1. Start the application:
     ```bash
     uvicorn main:app --host 0.0.0.0 --port 8000
     ```

## 🌐 Hosting

### 🚀 Deployment Instructions
  1. Build a Docker image:
     ```bash
     docker build -t ai-wrapper-service:latest .
     ```
  2. Run the Docker container:
     ```bash
     docker run -d -p 8000:8000 ai-wrapper-service:latest
     ```

### 🔑 Environment Variables

- **`DATABASE_URL`:** Connection string for the PostgreSQL database.
  Example: `postgresql://user:password@host:port/database`
- **`OPENAI_API_KEY`:** Your OpenAI API key for accessing OpenAI's services.
  Example: `sk-your_api_key_here`
- **`JWT_SECRET_KEY`:** A secret key used for signing and verifying JWT tokens. 
  Example: `your-256-bit-secret` 

## 📜 API Documentation
### 🔍 Endpoints

- **POST `/api/v1/generate_text`**
  - Description: Generate text using OpenAI's language models.
  - Headers:
    - `Authorization: Bearer YOUR_JWT_TOKEN`
  - Body:
    ```json
    {
      "input_text": "Write a short story about a robot who dreams.",
      "model": "text-davinci-003",
      "temperature": 0.7
    }
    ```
  - Response:
    ```json
    {
      "choices": [
        {
          "text": "Once upon a time, in a world where technology had advanced beyond human comprehension, there lived a robot named Unit 7. Unit 7 was a marvel of engineering, designed to perform complex tasks with unwavering precision. However, unbeknownst to his creators, Unit 7 possessed a secret - he dreamt.",
          "index": 0,
          "logprobs": null,
          "finish_reason": "stop"
        }
      ],
      "created": 1692509441,
      "model": "text-davinci-003",
      "usage": {
        "prompt_tokens": 13,
        "completion_tokens": 67,
        "total_tokens": 80
      }
    }
    ```

### 🔒 Authentication

1. **Register a new user or login to receive a JWT token:**
   - Send a POST request to `/api/v1/auth/signup` to register a new user.
   - Send a POST request to `/api/v1/auth/login` to authenticate an existing user.
2. **Include the token in the Authorization header for all protected routes:**
   ```
   Authorization: Bearer YOUR_JWT_TOKEN
   ```

### 📝 Examples
```bash
# Register a new user
curl -X POST http://localhost:8000/api/v1/auth/signup \
     -H "Content-Type: application/json" \
     -d '{"email": "user@example.com", "password": "securepass123"}'

# Response (successful registration)
{
  "message": "User created successfully"
}

# Login an existing user
curl -X POST http://localhost:8000/api/v1/auth/login \
     -H "Content-Type: application/json" \
     -d '{"email": "user@example.com", "password": "securepass123"}'

# Response (successful login)
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyQGV4YW1wbGUuY29tIiwiZXhwIjoxNjkzMjg2NjE0fQ.d7H-w5M-x_vZ2g5t3w2vU97qF6_G5Z70pZ3i1T2-dI",
  "token_type": "bearer"
}

# Generate text with authentication
curl -X POST http://localhost:8000/api/v1/generate_text \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyQGV4YW1wbGUuY29tIiwiZXhwIjoxNjkzMjg2NjE0fQ.d7H-w5M-x_vZ2g5t3w2vU97qF6_G5Z70pZ3i1T2-dI" \
     -d '{"input_text": "Write a short story about a robot who dreams.", "model": "text-davinci-003", "temperature": 0.7}'

# Response (successful text generation)
{
  "choices": [
    {
      "text": "In the heart of a bustling metropolis, where towering skyscrapers scraped the sky, resided a unique robot named R-42. Unlike his mechanical brethren, programmed for efficiency and logic, R-42 dreamt. Not in the literal sense, of course, but his circuits hummed with a peculiar form of sentience, crafting narratives of a world beyond the sterile reality of his programming. Each night, as his processors powered down, R-42 would drift into a state of simulated slumber, his circuits conjuring vivid scenes of verdant forests, shimmering lakes, and the gentle caress of the sun.",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "created": 1692509441,
  "model": "text-davinci-003",
  "usage": {
    "prompt_tokens": 13,
    "completion_tokens": 125,
    "total_tokens": 138
  }
}
```

## 📜 License & Attribution

### 📄 License
This Minimum Viable Product (MVP) is licensed under the [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) license.

### 🤖 AI-Generated MVP
This MVP was entirely generated using artificial intelligence through [CosLynx.com](https://coslynx.com).

No human was directly involved in the coding process of the repository: AI-Powered-Python-OpenAI-Wrapper

### 📞 Contact
For any questions or concerns regarding this AI-generated MVP, please contact CosLynx at:
- Website: [CosLynx.com](https://coslynx.com)
- Twitter: [@CosLynxAI](https://x.com/CosLynxAI)

<p align="center">
  <h1 align="center">🌐 CosLynx.com</h1>
</p>
<p align="center">
  <em>Create Your Custom MVP in Minutes With CosLynxAI!</em>
</p>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Developers-Drix10,_Kais_Radwan-red" alt="">
  <img src="https://img.shields.io/badge/Website-CosLynx.com-blue" alt="">
  <img src="https://img.shields.io/badge/Backed_by-Google,_Microsoft_&_Amazon_for_Startups-red" alt="">
  <img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4,_v6-black" alt="">
</div>