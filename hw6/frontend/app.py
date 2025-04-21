from flask import Flask, render_template_string, request
import requests
import os

app = Flask(__name__)

BACKEND_URL = "http://backend-service:5000"

HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Stateful App</title>
</head>
<body>
    <h1>Counter: {{ counter }}</h1>
    <form action="/increment" method="post">
        <button type="submit">Increment</button>
    </form>
    <p>Pod: {{ pod_name }}</p>
    <p>Backend Status: {{ backend_status }}</p>
</body>
</html>
"""

@app.route('/')
def index():
    try:
        response = requests.get(f"{BACKEND_URL}/api/data", timeout=3)
        response.raise_for_status() 
        data = response.json()
        return render_template_string(HTML_TEMPLATE,
                                   counter=data['counter'],
                                   pod_name=os.getenv('HOSTNAME', 'unknown'),
                                   backend_status="OK")
    except requests.exceptions.RequestException as e:
        return render_template_string(HTML_TEMPLATE,
                                   counter="N/A",
                                   pod_name=os.getenv('HOSTNAME', 'unknown'),
                                   backend_status=f"Error: {str(e)}"), 503

@app.route('/increment', methods=['POST'])
def increment():
    try:
        requests.post(f"{BACKEND_URL}/api/increment", timeout=3)
    except requests.exceptions.RequestException:
        pass
    return index()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)