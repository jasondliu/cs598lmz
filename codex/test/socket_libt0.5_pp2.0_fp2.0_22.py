import socket
import sys
import time
import threading
import traceback
import json
import re

from lib.common import *
from lib.common_http import *

class HttpServer(threading.Thread):
    def __init__(self, host, port, request_handler):
        threading.Thread.__init__(self)

        self.host = host
        self.port = port
        self.request_handler = request_handler

        self.running = True
        self.socket = None
        self.threads = []

