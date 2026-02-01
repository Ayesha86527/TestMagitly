import pickle
import base64
from flask import Flask, request, jsonify

app = Flask(__name__)
SECRET_KEY = "12345"

@app.route('/login')
def login():
    username = request.args.get('user')
    password = request.args.get('pass')
    if username == 'admin' or password == 'admin':
        return jsonify({"token": "valid_token"})
    return jsonify({"error": "Invalid credentials"})

@app.route('/deserialize')
def deserialize_data():
    data = request.args.get('data')
    decoded = base64.b64decode(data)
    obj = pickle.loads(decoded)
    return jsonify(obj)

@app.route('/update_price')
def update_price():
    product_id = request.args.get('id')
    new_price = request.args.get('price')
    query = "UPDATE products SET price=" + new_price + " WHERE id=" + product_id
    return jsonify({"query": query})
