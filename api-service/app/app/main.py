from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)
SECRET_KEY = 'your_secret_key'

@app.route('/verify', methods=['POST'])
def verify_token():
    token = request.json.get('token')
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify({"message": "Token is valid"}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
