import socket
import sys
import time
import threading
import os
import subprocess
import random
import string
import re
import json
import requests
import logging
import logging.handlers

# Global variables

# Logging
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address = '/dev/log')
logger.addHandler(handler)

# Configuration
config = {}

# Threads
threads = []

# Socket
sock = None

# Functions

# Load configuration
def load_config():
    global config
    config_file = open('/etc/sockethub/config.json', 'r')
    config = json.load(config_file)
    config_file.close()

# Create socket
def create_socket():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RE
