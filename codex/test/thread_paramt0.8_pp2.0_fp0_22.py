import sys, threading
threading.Thread(target=lambda: gevent.sleep(1e9)).start()
sys.argv = ['', 'test']
from greenlet import greenlet
import gevent
#import eventlet
#from eventlet import GreenletExit
from time import time
from flask import Flask,  render_template, jsonify, json, request
from flask.ext.socketio import SocketIO, emit, send
from flask.ext.cors import CORS
from datetime import datetime

from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Text, Binary, MetaData, ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import func


PORT = 5000

#class ServerError(Exception):
#    pass
#
#class NotFound(Exception):
#    pass

app = Flask(__name__)
