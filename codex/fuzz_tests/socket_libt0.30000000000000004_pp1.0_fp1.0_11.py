import socket
import sys
import os
import time
import threading
import random

# Server class
class Server:
    # Constructor
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        self.clients = {}
        self.addresses = {}
        self.list_of_users = []
        self.list_of_users_online = []
        self.list_of_users_offline = []
        self.list_of_users_blocked = []
        self.list_of_users_blocked_by = []
        self.list_of_users_online_blocked = []
        self.list_of_users_online_
