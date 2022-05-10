import socket
import threading
import time

class Server:
    def __init__(self, host, port):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the address given on the command line
        server_address = (host, port)
        print('starting up on {} port {}'.format(*server_address))
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(server_address)
        self.sock.listen(1)

        self.clients = []
        self.client_lock = threading.Lock()

        self.running = True

    def run(self):
        while self.running:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = self.sock.accept()
