import weakref
import threading
import signal
import time

import numpy as np
import pygame

from . import game
from . import actor
from . import vector

from .game import Game
from .actor import Actor


class PygameGame(Game):
    """
    A PygameGame is a game based on the Pygame library.
    It provides Pygame-specific methods and handles the Pygame event loop.
    """

    _clock = pygame.time.Clock()
    _key_handlers = {}
    _mouse_handlers = {}
    _handlers = {}

