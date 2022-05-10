import selectors
import socket
import types
import logging
import time
import sys
import threading
import queue
from common.messages import *
from common.utils import *
from server.utils import *
from server.database import *
import random
from server.game import Game

SERVER_ADDRESS = (HOST, PORT) = '', 8888

class Server:
    def __init__(self):
        self.sel = selectors.DefaultSelector()
        self.game = Game()
        self.create_server()


    def create_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(SERVER_ADDRESS)
        self.server_socket.listen()
        print('listening on', SERVER_ADDRESS)
        self.server_socket.setblocking(False)
        self.
