from flask import Flask, jsonify, request
import os
import json

app = Flask(__name__)

DATA_FILE = '/data/data.json'

def init_data():
    if not os.path.exists(os.path.dirname(DATA_FILE)):
        os.makedirs(os.path.dirname(DATA_FILE))
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump({"counter": 0}, f)

@app.route('/api/data', methods=['GET'])
def get_data():
    init_data()
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/increment', methods=['POST'])
def increment():
    init_data()
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    
    data['counter'] += 1
    
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)