import threading
threading.currentThread().setName('JuniorBot')
import time
import cPickle
from flask import Flask, Response
from tools import *

app = Flask(__name__)
app.debug = True
app.static_folder = "static"
app.static_folder = "templates"
app.logger_name = 'JuniorBot'


@app.route('/')
@app.route('/web')
def index():
    return render_template('index.html')

@app.route('/del', methods=['POST'])
def delt():
    global phone
    global lock
    try:
        lock.acquire()
        phone = []
    finally:
        lock.release()
    return 'Ok'


@app.route('/web/')
def web():
    res = ''
    try:
        lock.acquire()
        res = render_template('web.html', phones=phone)
    finally:
        lock.release()
    return  res


@app.route('/mobile')
def mobile():
    res =
