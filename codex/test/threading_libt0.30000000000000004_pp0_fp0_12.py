import threading
threading.stack_size(67108864)

from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_socketio import send, emit

from config import Config
from model import Model

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
socketio = SocketIO(app)

model = Model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    result = model.predict(data)
    return jsonify(result)

@socketio.on('connect')
def connect():
    print('connected')

@socketio.on('disconnect')
def disconnect():
    print('disconnected')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
