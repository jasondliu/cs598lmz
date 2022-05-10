import select
import socket
import sys
import threading
import time

import pygame

from . import constants
from . import events
from . import game
from . import graphics
from . import input
from . import network
from . import sound
from . import util
from . import world
from . import world_client
from . import world_server

class Client(object):
    def __init__(self):
        self.window = None
        self.world = None
        self.game = None
        self.network = None
        self.input = None
        self.graphics = None
        self.sound = None
        self.clock = None
        self.running = False
        self.server_address = None
        self.server_port = None
        self.player_name = None
        self.player_color = None
        self.player_number = None
        self.player_id = None
        self.player_ids = None
        self.player_names = None
        self.player_colors = None
        self.player_numbers = None
        self.player
