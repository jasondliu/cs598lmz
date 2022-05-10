import selectors
import socket
import types
import sys
import os
import json
import threading
from queue import Queue

from client import Client
from server import Server
from utils import *

class Chat:

    def __init__(self):
        self.sock = None
        self.server = None
        self.client = None
        self.server_port = None
        self.server_addr = None
        self.client_port = None
        self.client_addr = None
        self.selector = selectors.DefaultSelector()
        self.lock = threading.Lock()
        self.queue = Queue()

    def start_server(self, port, addr):
        self.server_port = port
        self.server_addr = addr
        self.server = Server(self.server_port, self.server_addr, self.selector, self.lock, self.queue)
        self.server.start()

    def start_client(self, port, addr, name):
        self.client_port = port
        self.client_addr = addr

