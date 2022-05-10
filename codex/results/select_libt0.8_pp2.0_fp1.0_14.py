import select, socket, sys, queue, json
import ssl, time
from datetime import datetime, timedelta
from functools import wraps
import argparse

class Server:
    def __init__(self, host="127.0.0.1", port=9090):
        self.host = host
        self.port = port
        self.queue = queue.Queue()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.settimeout(0.5)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.listen(5)
        self.inputs = [self.sock]
        self.outputs = []
        self.errors = []
        self.message_queues = {}
        self.clients = {}
        self.client_amount = {}
        self.running = True
        self.history
