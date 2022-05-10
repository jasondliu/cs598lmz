import socket
import threading
import time

from .config import Config
from .connection import Connection

class Client:

    def __init__(self, config: Config):
        self.config = config
        self.connection = Connection(config)
        self.threads = []
        self.running = False

    def connect(self):
        self.connection.connect()

    def disconnect(self):
        self.connection.disconnect()

    def start(self):
        self.running = True
        self.threads = [
            threading.Thread(target=self.handle_input),
            threading.Thread(target=self.handle_output),
        ]
        for thread in self.threads:
            thread.start()

    def stop(self):
        self.running = False
        for thread in self.threads:
            thread.join()

    def handle_input(self):
        while self.running:
            try:
                data = self.connection.read()
            except socket.error:
                break
            if not data:
                break
            print(
