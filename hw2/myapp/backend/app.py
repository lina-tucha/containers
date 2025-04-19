from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS 
import os
import time
from sqlalchemy.exc import OperationalError

app = Flask(__name__)
CORS(app) 

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/mydb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    if request.method == 'POST':
        content = request.json.get('content')
        if content:
            message = Message(content=content)
            db.session.add(message)
            db.session.commit()
            return jsonify({'status': 'success'})
        return jsonify({'status': 'error', 'message': 'Content is required'}), 400
    
    messages = Message.query.all()
    return jsonify([{'id': m.id, 'content': m.content} for m in messages])

if __name__ == '__main__':
    max_retries = 5
    retry_delay = 5
    
    for attempt in range(max_retries):
        try:
            with app.app_context():
                db.create_all()
            app.run(host='0.0.0.0', port=5000)
            break
        except OperationalError:
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
                continue
            raise