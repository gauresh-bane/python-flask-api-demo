# 🚀 Python Flask API Demo

![Flask](https://img.shields.io/badge/flask-3.0.0-green)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

A sample Flask REST API application designed to demonstrate AI-powered test automation capabilities. This API includes multiple endpoints for testing CRUD operations, filtering, and error handling.

## 📋 Overview

This Flask application provides a RESTful API with the following resources:
- **Users**: User management with CRUD operations
- **Posts**: Blog posts with author filtering
- **Products**: Product catalog with category filtering
- **Health Check**: System health monitoring

Perfect for testing with the [AI-Powered Test Automation Framework](https://github.com/gauresh-bane/ai-python-api-test-automation)!

## ✨ Features

- 🔄 Full CRUD operations on multiple resources
- 🔍 Query parameter filtering
- ✅ Input validation
- 🚨 Comprehensive error handling
- 📊 JSON responses
- 💾 In-memory data storage (for demo purposes)

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/gauresh-bane/python-flask-api-demo.git
cd python-flask-api-demo
```

2. **Create virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Running the Application

**Start the server:**
```bash
python app.py
```

The API will be available at `http://localhost:5000`

**With custom port:**
```bash
PORT=8080 python app.py
```

## 📚 API Endpoints

### Root Endpoint

#### GET /
Get API information and available endpoints.

**Response:**
```json
{
  "message": "Welcome to Flask API Demo",
  "version": "1.0.0",
  "endpoints": {
    "users": "/api/users",
    "posts": "/api/posts",
    "products": "/api/products",
    "health": "/api/health"
  }
}
```

### Health Check

#### GET /api/health
Check API health status.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-10-24T11:00:00.000000",
  "service": "flask-api-demo"
}
```

### Users API

#### GET /api/users
Get all users.

**Response:**
```json
{
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "role": "admin"
    }
  ],
  "count": 1
}
```

#### GET /api/users/{id}
Get a specific user by ID.

**Example:** `GET /api/users/1`

**Response:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "role": "admin"
}
```

#### POST /api/users
Create a new user.

**Request Body:**
```json
{
  "name": "Alice Brown",
  "email": "alice@example.com",
  "role": "user"
}
```

**Response:** `201 Created`
```json
{
  "id": 4,
  "name": "Alice Brown",
  "email": "alice@example.com",
  "role": "user"
}
```

#### PUT /api/users/{id}
Update an existing user.

**Request Body:**
```json
{
  "name": "John Updated",
  "role": "superadmin"
}
```

**Response:**
```json
{
  "id": 1,
  "name": "John Updated",
  "email": "john@example.com",
  "role": "superadmin"
}
```

#### DELETE /api/users/{id}
Delete a user.

**Response:**
```json
{
  "message": "User deleted successfully"
}
```

### Posts API

#### GET /api/posts
Get all posts.

**Query Parameters:**
- `author_id` (optional): Filter posts by author ID

**Example:** `GET /api/posts?author_id=1`

**Response:**
```json
{
  "posts": [
    {
      "id": 1,
      "title": "First Post",
      "content": "This is the first post",
      "author_id": 1,
      "created_at": "2025-10-24T10:00:00Z"
    }
  ],
  "count": 1
}
```

#### GET /api/posts/{id}
Get a specific post by ID.

#### POST /api/posts
Create a new post.

**Request Body:**
```json
{
  "title": "New Post",
  "content": "This is a new post",
  "author_id": 1
}
```

### Products API

#### GET /api/products
Get all products.

**Query Parameters:**
- `category` (optional): Filter products by category

**Example:** `GET /api/products?category=Electronics`

**Response:**
```json
{
  "products": [
    {
      "id": 1,
      "name": "Laptop",
      "price": 999.99,
      "stock": 50,
      "category": "Electronics"
    }
  ],
  "count": 1
}
```

#### GET /api/products/{id}
Get a specific product by ID.

#### POST /api/products
Create a new product.

**Request Body:**
```json
{
  "name": "Keyboard",
  "price": 79.99,
  "stock": 100,
  "category": "Electronics"
}
```

## 🧪 Testing with AI-Powered Framework

This API is designed to work with the [AI-Powered Test Automation Framework](https://github.com/gauresh-bane/ai-python-api-test-automation).

### Setup Test Framework

1. **Clone the test framework:**
```bash
git clone https://github.com/gauresh-bane/ai-python-api-test-automation.git
cd ai-python-api-test-automation
```

2. **Install test dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure the API base URL:**
Update the base URL in test configuration to point to `http://localhost:5000`

4. **Run tests with Allure reporting:**
```bash
pytest --alluredir=reports/allure-results
```

5. **View Allure reports:**
```bash
allure serve reports/allure-results
```

### Example Test Case

```python
import pytest
import allure
import requests

BASE_URL = "http://localhost:5000"

@allure.feature('Users API')
@allure.story('Get All Users')
@allure.severity(allure.severity_level.CRITICAL)
def test_get_all_users():
    """Test retrieving all users from the API"""
    
    with allure.step('Send GET request to /api/users'):
        response = requests.get(f"{BASE_URL}/api/users")
        allure.attach(str(response.json()), name="Response", 
                     attachment_type=allure.attachment_type.JSON)
    
    with allure.step('Verify status code is 200'):
        assert response.status_code == 200
    
    with allure.step('Verify response contains users'):
        data = response.json()
        assert "users" in data
        assert "count" in data
        assert data["count"] > 0
```

## 🔧 Error Handling

The API returns appropriate HTTP status codes:

- `200 OK`: Successful GET, PUT requests
- `201 Created`: Successful POST requests
- `400 Bad Request`: Invalid input data
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server errors

**Error Response Format:**
```json
{
  "error": "Error message description"
}
```

## 📊 Sample Data

The API comes pre-loaded with sample data:

**Users:**
- 3 users (1 admin, 2 regular users)

**Posts:**
- 2 blog posts

**Products:**
- 3 products (2 Electronics, 1 Furniture)

## 🛠️ Development

### Project Structure

```
python-flask-api-demo/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore file
└── README.md          # This file
```

### Adding New Endpoints

1. Define the route in `app.py`:
```python
@app.route('/api/your-endpoint', methods=['GET'])
def your_function():
    # Your logic here
    return jsonify({"message": "Success"})
```

2. Test the endpoint
3. Update this README with documentation

## 📝 Notes

- **Data Persistence**: This demo uses in-memory storage. Data resets when the server restarts.
- **Production Use**: For production, integrate with a database (PostgreSQL, MongoDB, etc.)
- **Security**: Add authentication, rate limiting, and input sanitization for production use.

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Add new endpoints or improve existing ones
4. Submit a pull request

## 📄 License

MIT License - Free to use for learning and testing purposes.

## 🔗 Related Projects

- [AI-Powered Test Automation Framework](https://github.com/gauresh-bane/ai-python-api-test-automation) - Use this to test the API

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Happy Testing! 🚀**
