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

    def run(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)

            while self.running:
                try:
                    conn, addr = self.socket.accept()
                    client = HttpClient(conn, addr, self
