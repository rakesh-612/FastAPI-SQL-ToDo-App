Create a .env file in the root of your project and add the following:
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/fastapi_todo

Details:
Username: postgres,
Password: YOUR_PASSWORD (replace with your actual PostgreSQL password),
Host: localhost,
Port: 5432,
Database Name: fastapi_todo


# FastAPI Todo App Setup

---

## 📁 Create Project Folder

YOUR_WORKSPACE_PATH> mkdir fastapi-todo-app  

---

## 🧪 Create Virtual Environment

YOUR_WORKSPACE_PATH> python -m venv post-env  

Activate environment:

YOUR_WORKSPACE_PATH> .\post-env\Scripts\activate  

---

## 📥 Install Dependencies

Install FastAPI and required packages:

(post-env) YOUR_WORKSPACE_PATH> python -m pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv  

Install Pydantic:

(post-env) YOUR_WORKSPACE_PATH> pip install pydantic  

---

## ▶️ Run the Project

(post-env) YOUR_WORKSPACE_PATH\fastapi-todo-app> uvicorn main:app --host 0.0.0.0 --port 8000 --reload  

App will run at:  
http://127.0.0.1:8000/  

---

## 📦 Create Requirements File

(post-env) YOUR_WORKSPACE_PATH\fastapi-todo-app> pip freeze > requirements.txt  

---

## ☁️ Deployment (Render)

Go to: https://render.com  

Steps:
- Create a new service  
- Choose **PostgreSQL**  
- Name: `fastapi-todo`  
- Database: `todos`  

---

## 📌 Notes

- Ensure virtual environment is activated before running commands  
- Use `.env` file for environment variables  
- Make sure PostgreSQL is configured properly

Reference: https://youtu.be/41bRmKMb464
