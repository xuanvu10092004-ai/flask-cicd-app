# Sử dụng Python image chính thức (bản slim nhẹ hơn)
FROM python:3.11-slim

# Thư mục làm việc trong container
WORKDIR /app

# Copy requirements trước để tận dụng Docker cache layer
COPY requirements.txt .

# Cài dependencies (--no-cache-dir giảm kích thước image)
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ source code vào container
COPY . .

# Expose port Flask chạy
EXPOSE 5000

# Lệnh chạy khi container start
CMD ["python", "app.py"]
