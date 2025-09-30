from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/submit', methods=['POST'])
def handle_form():
    data = request.json
    print(f"Received data from frontend: {data}")

    name = data.get('name')
    email = data.get('email')

    response_data = {
        "message": "Data received successfully by flask!",
        "processed_data": {"name": name, "email": email}
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
