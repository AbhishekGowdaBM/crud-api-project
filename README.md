# CRUD API with FastAPI and SQLite

## Features

- Full CRUD for items
- SQLite for storage
- FastAPI with Swagger UI at `/docs`
- Dockerized
- Ready for Tekton CI/CD

## 🔧 Local Setup

```bash
git clone https://github.com/yourusername/crud-api-app.git
cd crud-api-app
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Visit: http://localhost:8000/docs

## 🐳 Docker Setup

```bash
docker build -t crud-api-app .
docker run -d -p 8000:8000 crud-api-app
```

## 🔁 Push to DockerHub

```bash
docker tag crud-api-app abhishekgowdabm/crud-api-app
docker login
docker push abhishekgowdabm/crud-api-app
```
