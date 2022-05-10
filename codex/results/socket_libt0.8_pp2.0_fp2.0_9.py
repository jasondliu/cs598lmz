import socket
import sys
import threading
import time


class ServerClass:
    def __init__(self, port, caddy):
        self.port = port
        self.caddy = caddy
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('', port))
        self.sock.listen(1)
        self.server_thread = threading.Thread(target=self.handle_listen)
        self.server_thread.daemon = True
        self.server_thread.start()

    def stop(self, timeout=None):
        self.sock.close()
        self.server_thread.join(timeout=timeout)

    def handle_listen(self):
        try:
            while True:
                # Accept a connection from an incoming client
                client, address = self.sock.accept()
                handle_client_thread
