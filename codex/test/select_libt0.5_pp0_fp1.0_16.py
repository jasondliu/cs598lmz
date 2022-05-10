import select
import socket
import sys
import traceback
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

from lib.config import Config
from lib.logger import Logger
from lib.utils import Utils

class Server:

    def __init__(self):
        self.logger = Logger()
        self.config = Config()
        self.utils = Utils()
        self.peers = []

    def run(self):
        try:
            self.server = HTTPServer((self.config.get('ip'), self.config.get('port')), Handler)

            self.server.serve_forever()

        except KeyboardInterrupt:
            self.server.socket.close()


class Handler(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        self.logger = Logger()
        self.config = Config()
        self.utils = Utils()
        self.peers = []

        super().__init__(*args, **kwargs)

