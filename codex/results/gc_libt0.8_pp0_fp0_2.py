import gc, weakref

import pygame

try:
    import cPickle as _pickle
except ImportError:
    import pickle as _pickle

from gameobjects.vector2 import *

import config

from actors import *
from statics import *
from projectiles import *

from util import *

MAIN_LEVEL = "data/levels/main1.level"

class GameController:

    screen = None
    font = None
    backdrop = None
    backyard = None
    bg_x = -400
    bg_y = 0
    
    paused = False
    playmode = True
    endingscreen = False
    
    def init_graphics(self):
        """Initialize the graphics system"""
        pygame.init()
        pygame.mixer.init()
        screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("Nouveau Hero")
        self.backdrop = pygame.image.load("data/g
