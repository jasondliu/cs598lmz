import socket
import time
import threading
import random
import json
import os
import csv
import sys

random.seed(0)

PORT = 1337
HOST = "127.0.0.1"

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
# s.sendall(b'Hello, world')
# data = s.recv(1024)

# s.close()

# print(repr(data))

# Message to send over TCP

class Player:
    def __init__(self):
        self.id = id
        self.y = 0
        self.x = 0
        self.score = 0
        self.direction = 0
        self.sprite = ""

class GameState:
    def __init__(self):
        self.status = "waiting..."
        self.players = []
        self.grid = []
        self.speed = "0.2"
        self.score = "0"
