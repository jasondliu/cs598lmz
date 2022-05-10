import socket
import sys

from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flask_cors import CORS

from utils import *
from models import *

app = Flask(__name__)
api = Api(app)
CORS(app)

class Home(Resource):
    def get(self):
        return render_template('index.html')

class GetAll(Resource):
    def get(self):
        return list(map(lambda x: x.json(), User.query.all()))

class GetOne(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        return user.json() if user else f'User with id {id} not found', 404

class CreateUser(Resource):
    def post(self):
        data = request.get_json()
