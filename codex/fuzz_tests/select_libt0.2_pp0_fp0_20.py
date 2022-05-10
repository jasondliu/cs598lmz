import select
import socket
import sys
import time
import threading
import traceback

import pygame
from pygame.locals import *

from common import *
from config import *
from game import *
from network import *
from player import *
from server import *
from ui import *

class Client(object):
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.game = None
        self.player = None
        self.socket = None
        self.ui = None
        self.running = False
        self.clock = pygame.time.Clock()
        self.last_update = 0
        self.last_draw = 0
        self.last_fps = 0
        self.fps = 0
        self.fps_counter = 0
        self.fps_counter_time = 0
        self.fps_counter_time_start = 0
        self.fps_counter_time_end = 0
        self.fps_counter_time_diff = 0
        self
