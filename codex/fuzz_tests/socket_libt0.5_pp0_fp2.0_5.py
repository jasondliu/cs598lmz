import socket
import sys
import threading
import time
import urllib

class ServerThread(threading.Thread):
    def __init__(self, server_address, server_port, buffer_size, request_queue_size, client_address, client_port, client_buffer_size, client_request_queue_size):
        threading.Thread.__init__(self)
        self.server_address = server_address
        self.server_port = server_port
        self.buffer_size = buffer_size
        self.request_queue_size = request_queue_size
        self.client_address = client_address
        self.client_port = client_port
        self.client_buffer_size = client_buffer_size
        self.client_request_queue_size = client_request_queue_size

    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.server_address, self.server_port))
        server_socket.listen(self.
