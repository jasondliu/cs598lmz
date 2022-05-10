import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
import os
import json
import random
import datetime
import traceback
import logging
import logging.handlers
import socket
import argparse
import configparser

# import the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pyvivint

# get the logger
logger = logging.getLogger(__name__)

# set the default logging level
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.handlers.RotatingFileHandler('vivint_sensor_monitor.log', maxBytes=10000000, backupCount=5)
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

