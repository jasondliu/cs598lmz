import threading
threading.stack_size(67108864)

import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from flask import Flask, render_template, json, request, redirect, session, jsonify
from werkzeug import generate_password_hash, check_password_hash
from datetime import datetime
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('localhost', 27017)

def run_on_startup():
    try:
        db = client.test
        print("Successfully connected to MongoDB")
    except ConnectionFailure as e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)

run_on_startup()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

