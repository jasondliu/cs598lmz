import socket
import sys
import threading
import time

import pygame

from settings import *
from player import Player, PlayerState
from game import Game
from bullet import Bullet
from map import Map
from powerup import Powerup
from server import Server

class Client(threading.Thread):
    def __init__(self, game, host, port, name):
        threading.Thread.__init__(self)
        self.game = game
        self.host = host
        self.port = port
        self.name = name
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.sock.send(self.name.encode())
        self.running = True

    def run(self):
        while self.running:
            data = self.sock.recv(1024)
            if data:
                data = data.decode()
                data = data.split('|')
