import select
import socket
import time
import sys
import os
import errno

#import pygame
#from pygame.locals import *

from threading import Thread

from player import Player

class Server:
    def __init__(self, port=4040, num_players=2, timeout=5, verbose=True):
        self.port = port
        self.num_players = num_players
        self.timeout = timeout
        self.verbose = verbose
        self.players = []
        self.started = False
        self.running = True
        self.go_next = False
        self.go_next_timer = 0
        self.go_next_time = 0.5
        self.go_next_time_max = 1.0
        self.go_next_time_step = 0.1
        self.go_next_time_step_max = 0.5
        self.go_next_time_step_inc = 0.1
        self.go_next_time_step_inc_max = 0.5
        self.go
