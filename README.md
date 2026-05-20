# Flask CI/CD App

Ứng dụng Flask mẫu với pipeline CI/CD hoàn chỉnh.

## Cấu trúc project

```
flask-cicd-app/
├── app.py                          # Flask application
├── requirements.txt                # Python dependencies
├── test_app.py                     # Unit tests
├── Dockerfile                      # Docker image config
├── docker-compose.yml              # Docker Compose config
└── .github/
    └── workflows/
        └── ci-cd.yml              # GitHub Actions pipeline
```

## Chạy local (không Docker)

```bash
pip install -r requirements.txt
python app.py
```

Truy cập: http://localhost:5000

## Chạy local bằng Docker

```bash
# Build image
docker build -t flask-cicd-app .

# Run container
docker run -p 5000:5000 flask-cicd-app
```

## Chạy test

```bash
pytest
```

## CI/CD Pipeline

Khi push code lên branch `main`:
1. GitHub Actions tự động chạy test
2. Build Docker image
3. Push lên Docker Hub
4. SSH vào server và deploy
