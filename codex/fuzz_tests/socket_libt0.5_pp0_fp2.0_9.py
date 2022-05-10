import socket
import sys
import threading
import time
import os
import re
import random
import math
from pynput.keyboard import Key, Listener

#Global variables
global_counter = 0
global_turn = 0

#Server class
class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((self.host, self.port))
        self.server.listen(10)
        self.list_of_clients = []
        self.list_of_names = []
        self.list_of_clients_ready = []
        self.current_player = 0

    #Function to send message to all clients
    def broadcast(self, message):
        for client in self.list_of_clients:
            client.send(
