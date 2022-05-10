import select
import socket
import sys
import time

from collections import deque

import pygame

from pygame.locals import *

class NetworkError(Exception):
    pass

class NetworkManager(object):
    def __init__(self, host, port, name, on_connect=None, on_disconnect=None,
                 on_data=None, on_error=None):
        self.host = host
        self.port = port
        self.name = name
        self.on_connect = on_connect
        self.on_disconnect = on_disconnect
        self.on_data = on_data
        self.on_error = on_error

        self.connected = False
        self.connecting = False
        self.socket = None
        self.buffer = deque()

    def connect(self):
        if self.connecting:
            return
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
           
