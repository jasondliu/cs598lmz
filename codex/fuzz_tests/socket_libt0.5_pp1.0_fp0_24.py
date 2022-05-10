import socket
import select
import sys
import datetime
import time
import random
import threading
import json
import logging
import logging.handlers

# Logging
logger = logging.getLogger('server')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('server.log')
fh.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to logger
logger.addHandler(fh)
logger.addHandler(ch)

# Server
HOST = '127.0.0.1'
PORT = 8888

# User
user_list = []
