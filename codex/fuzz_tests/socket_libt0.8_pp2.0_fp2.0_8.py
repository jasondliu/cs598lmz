import socket
import logging
import argparse

from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

from logger import logger
from helpers import *


application = Flask(__name__)
CORS(application)
api = Api(application)
logger.setLevel(logging.INFO)


class HelloWorld(Resource):
    def get(self):
        logger.info("Hello there!")
        return greetings()


class Example(Resource):
    def get(self, user_name):
        logger.info("Hello there, %s!", user_name)
        return greetings(user_name)


class HealthCheck(Resource):
    def get(self):
        return "I'm feeling great!"


api.add_resource(HelloWorld, '/')
api.add_resource(Example, '/<string:user_name>')
api.add_resource(HealthCheck, '/healthcheck')


@application.after_request
def apply_caching(response):
    response.headers['Access-Control-Allow-
