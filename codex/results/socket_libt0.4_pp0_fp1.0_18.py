import socket
import sys
import threading
import time

from common import *
from config import *
from message import *
from peer import *

class Server:
    def __init__(self):
        self.peer_list = []
        self.peer_list_lock = threading.Lock()

        self.message_list = []
        self.message_list_lock = threading.Lock()

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
        self.server_socket.listen(SERVER_BACKLOG)

    def listen(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            client_thread = threading.Thread(target = self.client_handler, args = (client_socket, client_address))
            client_
