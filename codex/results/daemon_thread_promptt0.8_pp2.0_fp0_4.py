import threading
# Test threading daemon
import time
import sys

import requests
from requests.exceptions import ConnectionError
import json

from monitor import Monitor

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = ThreadedTCPServer((self.host, self.port), ThreadedTCPRequestHandler)

    def start(self):
        # Start a thread with the server
        # That thread will then start one
        # more thread for each request
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()
        print("Server loop running in thread:", self.server_thread.name)

    def stop(self):
        self.server.shutdown()

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        if not data:
            print('Empty request')
