import threading
threading.stack_size(102400)


import time
import pymysql

from flask import Flask, render_template, request, redirect, url_for, send_from_directory

from werkzeug import secure_filename
from face_detection import face_detection
from face_training import face_training
from FR_system import FR_system

from flask_bootstrap import Bootstrap

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
bootstrap = Bootstrap(app)


app.config['UPLOAD_FOLDER'] = 'face_image/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['RESULT_FOLDER'] = 'result/'
app.config['FINAL_FOLDER'] = 'final/'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in
