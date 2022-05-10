import mmap
import os
import sys
import time
import traceback

import pygame
from pygame.locals import *

from . import constants
from . import data
from . import game
from . import graphics
from . import input
from . import sound
from . import util

class Engine(object):
    def __init__(self):
        self.running = False
        self.paused = False
        self.clock = pygame.time.Clock()
        self.screen = None
        self.game = None
        self.input = None
        self.graphics = None
        self.sound = None

    def start(self):
        self.running = True
        self.paused = False
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT),
            pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE,
            32)
        self.game = game.Game
