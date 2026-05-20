from flask import Flask

# Khởi tạo Flask app
app = Flask(__name__)

# Route trang chủ
@app.route("/")
def home():
    return "Hello CI/CD Flask App!"

# Chạy app
if __name__ == "__main__":
    # host=0.0.0.0 để container bên ngoài truy cập được
    app.run(host="0.0.0.0", port=5000)
