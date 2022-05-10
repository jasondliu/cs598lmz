import mmap
+import random
+import logging
+import io
+import json
+import socketio
+import os.path
+import datetime
+from urllib.parse import urlparse
+from logging.handlers import RotatingFileHandler
+
+from flask import Flask, request, Response
+from flask_cors import CORS
+from requests import Request, Session
+from flask_sockets import Sockets
+
+app = Flask(__name__)
+app.config['SECRET_KEY'] = 'secret!'
+
+sio = socketio.Server()
+sockets = Sockets(app)
+
+CORS(app, resources={r'/*': {'origins': '*'}})
+
+cams = {}
+
+logger = logging.getLogger('werkzeug')
+logger.setLevel(logging.WARNING)
+handler = RotatingFileHandler('root.log', maxBytes=10000, backupCount=5)
+handler.setLevel(logging.DEBUG)
+handler.setFormatter(logging.Form
