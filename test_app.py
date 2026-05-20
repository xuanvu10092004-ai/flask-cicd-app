from app import app

# Tạo test client
client = app.test_client()

def test_home():
    response = client.get("/")

    # Kiểm tra HTTP status
    assert response.status_code == 200

    # Kiểm tra nội dung trả về
    assert b"Hello CI/CD Flask App!" in response.data
