import select
import socket
import sys
import threading
import time
import traceback

import pygame

import config
import game
import net
import player
import protocol
import util

# The server is a singleton.
_server = None

def get_server():
    global _server
    if _server is None:
        _server = Server()
    return _server

class Server(object):
    def __init__(self):
        self.game = game.Game()
        self.players = {}
        self.player_ids = []
        self.player_id_counter = 0
        self.listen_socket = None
        self.listen_thread = None
        self.running = False
        self.last_tick = 0
        self.tick_rate = config.TICK_RATE
        self.tick_interval = 1.0 / self.tick_rate
        self.tick_thread = None
        self.tick_lock = threading.Lock()
        self.tick_event = threading.Event()
        self.tick_event.set()
