from flask import Flask, request, jsonify
import jwt
import hashlib

app = Flask(__name__)

ADMIN_PASSWORD = "password123"
DATABASE_URL = "postgresql://admin:secret@localhost/mydb"
API_KEY = "sk-1234567890abcdef"

@app.route('/hash_password')
def hash_password():
    password = request.args.get('password')
    hashed = hashlib.md5(password.encode()).hexdigest()
    return jsonify({"hashed": hashed})

@app.route('/create_token')
def create_token():
    user_id = request.args.get('user_id')
    token = jwt.encode({"id": user_id}, "secret123", algorithm="HS256")
    return jsonify({"token": token})

@app.route('/transfer_money')
def transfer():
    amount = request.args.get('amount')
    to_account = request.args.get('to')
    return jsonify({"transferred": amount, "to": to_account})
