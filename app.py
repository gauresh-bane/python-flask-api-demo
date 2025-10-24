from flask import Flask, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)

# In-memory data store
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "role": "admin"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "role": "user"},
    {"id": 3, "name": "Bob Johnson", "email": "bob@example.com", "role": "user"}
]

posts = [
    {"id": 1, "title": "First Post", "content": "This is the first post", "author_id": 1, "created_at": "2025-10-24T10:00:00Z"},
    {"id": 2, "title": "Second Post", "content": "Another interesting post", "author_id": 2, "created_at": "2025-10-24T11:00:00Z"},
]

products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "stock": 50, "category": "Electronics"},
    {"id": 2, "name": "Mouse", "price": 29.99, "stock": 200, "category": "Electronics"},
    {"id": 3, "name": "Desk", "price": 299.99, "stock": 15, "category": "Furniture"},
]

# Routes
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Flask API Demo",
        "version": "1.0.0",
        "endpoints": {
            "users": "/api/users",
            "posts": "/api/posts",
            "products": "/api/products",
            "health": "/api/health"
        }
    })

@app.route('/api/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "flask-api-demo"
    })

# User endpoints
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({"users": users, "count": len(users)})

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    new_id = max([u['id'] for u in users]) + 1 if users else 1
    new_user = {
        "id": new_id,
        "name": data['name'],
        "email": data['email'],
        "role": data.get('role', 'user')
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    user.update({k: v for k, v in data.items() if k != 'id'})
    return jsonify(user)

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    users = [u for u in users if u['id'] != user_id]
    return jsonify({"message": "User deleted successfully"}), 200

# Post endpoints
@app.route('/api/posts', methods=['GET'])
def get_posts():
    author_id = request.args.get('author_id', type=int)
    if author_id:
        filtered_posts = [p for p in posts if p['author_id'] == author_id]
        return jsonify({"posts": filtered_posts, "count": len(filtered_posts)})
    return jsonify({"posts": posts, "count": len(posts)})

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return jsonify(post)
    return jsonify({"error": "Post not found"}), 404

@app.route('/api/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    if not data or 'title' not in data or 'content' not in data or 'author_id' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    new_id = max([p['id'] for p in posts]) + 1 if posts else 1
    new_post = {
        "id": new_id,
        "title": data['title'],
        "content": data['content'],
        "author_id": data['author_id'],
        "created_at": datetime.now().isoformat() + "Z"
    }
    posts.append(new_post)
    return jsonify(new_post), 201

# Product endpoints
@app.route('/api/products', methods=['GET'])
def get_products():
    category = request.args.get('category')
    if category:
        filtered_products = [p for p in products if p['category'].lower() == category.lower()]
        return jsonify({"products": filtered_products, "count": len(filtered_products)})
    return jsonify({"products": products, "count": len(products)})

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    required_fields = ['name', 'price', 'stock', 'category']
    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    
    new_id = max([p['id'] for p in products]) + 1 if products else 1
    new_product = {
        "id": new_id,
        "name": data['name'],
        "price": float(data['price']),
        "stock": int(data['stock']),
        "category": data['category']
    }
    products.append(new_product)
    return jsonify(new_product), 201

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
