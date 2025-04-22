from flask import Flask, request, jsonify
import requests
import json
from flask_cors import CORS
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"], supports_credentials=True)

# Simulated user database
users = {"ap11@gmail.com": "password123"}

SYSTEM_PROMPT = """
You are an expert legal advisor specializing in Indian law including IPC, labor laws, tenancy acts, family law, consumer protection, and related civil/criminal procedures.
Your job is to provide clear, accessible legal guidance to everyday users who may not have prior legal knowledge.
...
"""

def query_ollama(user_prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            headers={"Content-Type": "application/json"},
            data=json.dumps({
                "model": "gemma:2b",
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ],
                "stream": False
            })
        )
        if response.status_code == 200:
            return response.json()["message"]["content"]
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: Failed to connect to Ollama service - {str(e)}"

@app.route('/api/query', methods=['POST'])
def get_legal_advice():
    data = request.get_json()
    user_prompt = data.get('query', '')
    response = query_ollama(user_prompt)
    return jsonify({'response': response})

@app.route('/google-auth', methods=['POST'])
def google_auth():
    credential = request.json.get('credential')
    try:
        CLIENT_ID = "354642305939-v1f3pip41r9hgns38ptmo2e53egesi14.apps.googleusercontent.com"
        id_info = id_token.verify_oauth2_token(credential, google_requests.Request(), CLIENT_ID)
        email = id_info['email']
        return jsonify({"success": True, "email": email})
    except ValueError as e:
        return jsonify({"success": False, "error": str(e)}), 400

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        print(f"Register request: {data}")
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({'success': False, 'error': 'Missing email or password'}), 400
        email = data['email']
        password = data['password']
        if email in users:
            return jsonify({'success': False, 'error': 'Email already exists'}), 400
        if len(password) < 6:
            return jsonify({'success': False, 'error': 'Password must be at least 6 characters'}), 400
        users[email] = password
        print(f"Users after register: {users}")
        return jsonify({'success': True})
    except Exception as e:
        print(f"Register error: {e}")
        return jsonify({'success': False, 'error': 'Server error during registration'}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        print(f"Login request: {data}")
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({'success': False, 'error': 'Missing email or password'}), 400
        email = data['email']
        password = data['password']
        print(f"Checking login: Email={email}, Password={password}, Users={users}")
        if email in users and users[email] == password:
            print(f"Login successful for {email}")
            return jsonify({'success': True, 'email': email})
        print(f"Login failed for {email}, users: {users}")
        return jsonify({'success': False, 'error': 'Invalid credentials'}), 400
    except Exception as e:
        print(f"Login error: {e}")
        return jsonify({'success': False, 'error': 'Server error during login'}), 500

@app.route('/reset-password', methods=['POST'])
def reset_password():
    try:
        data = request.get_json()
        print(f"Reset request: {data}")
        if not data or 'email' not in data or 'newPassword' not in data:
            return jsonify({'success': False, 'error': 'Missing email or new password'}), 400
        email = data['email']
        new_password = data['newPassword']
        if email not in users or len(new_password) < 6:
            return jsonify({'success': False, 'error': 'Invalid email or password too short'}), 400
        users[email] = new_password
        print(f"Users after reset: {users}")
        return jsonify({"success": True, "message": "Password updated"})
    except Exception as e:
        print(f"Reset error: {e}")
        return jsonify({'success': False, 'error': 'Server error during reset'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)