import socket
from flask import Flask
from flask import request
import json
from flask import jsonify
from flask import make_response
from flask import Response
from flask_cors import CORS
import requests
from flask import abort
from flask import render_template
import urllib2
import datetime
import time
from flask import redirect
from flask import url_for

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/api/v1/users', methods=['PUT'])
def add_user():
    if request.method == 'PUT':
        data = request.get_json()
        if 'username' in data and 'password' in data:
            if len(data['username']) == 0 or len(data['password']) == 0:
                return Response(status=400)
            else:
                username = data['username']
                password = data['password']
                with open('users.txt', 'r') as f:
                    content = f.
