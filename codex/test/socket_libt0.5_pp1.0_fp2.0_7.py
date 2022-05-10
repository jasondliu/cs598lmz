import socket
import sys
import time
import random

from threading import Thread

class Bot:
    """
    A bot that connects to a server and sends it random commands.
    """

    def __init__(self, server_address, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((server_address, port))
        self.running = True
        self.thread = Thread(target=self.run)
        self.thread.start()

    def run(self):
        """
        Sends commands to the server.
        """
        while self.running:
            if random.random() < 0.3:
                self.socket.sendall(b'GET\n')
            else:
                self.socket.sendall(b'SET\n')
            time.sleep(0.1)

    def stop(self):
        """
        Stops the bot.
        """
        self.running = False


