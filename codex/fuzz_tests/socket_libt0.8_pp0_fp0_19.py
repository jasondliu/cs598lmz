import socket

from flask import Flask, request, jsonify
from flask_cors import CORS

from .. import modules
from ..models import user

app = Flask(__name__)
CORS(app)


@app.route('/home/<repo_slug>', methods=['GET'])
def get_home_page(repo_slug):
    return modules.get_modules_home_page(repo_slug)


@app.route('/add/', methods=['POST'])
def add_module():
    url = request.get_json()['url']
    return modules.add_module(url)


@app.route('/delete/', methods=['DELETE'])
def delete_module():
    repo_id = request.get_json()['id']
    return modules.remove_module(repo_id)


@app.route('/login/', methods=['POST'])
def login():
    username = request.get_json()['username']
    password = request.get_json()['password']
   
