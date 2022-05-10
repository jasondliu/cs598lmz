import socket
import sys
import time
import random
import threading
import hashlib
import struct

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, self.port))
        self.sock.setblocking(False)
        self.sock.settimeout(0.1)
        self.player_id = -1
        self.player_name = ""
        self.player_color = (0, 0, 0)
        self.players = {}
        self.player_lock = threading.Lock()
        self.recv_thread = threading.Thread(target=self.recv_game_state)
        self.recv_thread.start()

    def send_data(self, data):
        try:
            self.sock.sendall(data)
        except socket.error:
            sys.exit()

