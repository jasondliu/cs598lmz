import ctypes
import ctypes.util
import threading
import sqlite3
from flask import Flask, request, jsonify, Response, render_template, send_from_directory
from flaskext.mysql import MySQL
from flask_cors import CORS, cross_origin
from werkzeug import secure_filename
import os

app = Flask(__name__)
CORS(app)
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'phone_book'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


# upload folder
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ctype lib
libc = ctypes.CDLL(ctypes.util.find_library('c'))
_set_thread_
