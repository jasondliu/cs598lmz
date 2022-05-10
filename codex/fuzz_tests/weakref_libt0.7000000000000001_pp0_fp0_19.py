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

    def __init__(self, caption=None, width=640, height=480, fps=60,
                 fullscreen=False, background_color=None,
                 show_frame_rate=False, show_collision_boxes=False):
        """
        Constructs a new PygameGame.

        :param caption: title of the window
        :param width: width of the window
        :param height: height of the window
        :param fps: frames per second for the game
        :param fullscreen: True
