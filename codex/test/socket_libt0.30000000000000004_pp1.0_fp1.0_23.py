import socket
import threading
import time
import sys
import os

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 server.py <port>")
        return

    port = int(sys.argv[1])
    server = Server(port)
    server.start()

class Server:
    def __init__(self, port):
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(("127.0.0.1", port))
        self.server_socket.listen(5)
        self.threads = []
        self.connections = []
        self.lock = threading.Lock()

    def start(self):
        print("Server started on port {}".format(self.port))
