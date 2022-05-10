import ctypes
import ctypes.util
import threading
import sqlite3
import os

import pygame

from . import constants
from . import graphics
from . import data
from . import tiles
from . import world


def _initialize_game():
    """Initialize the game.

    This should be called as soon as possible after starting the game.
    """
    # Initialize SDL
    if not pygame.display.get_init():
        if pygame.display.init() < 0:
            raise RuntimeError("Couldn't initialize display")
    if not pygame.font.get_init():
        if pygame.font.init() < 0:
            raise RuntimeError("Couldn't initialize font")
    if not pygame.mixer.get_init():
        if pygame.mixer.init() < 0:
            raise RuntimeError("Couldn't initialize mixer")
    if not pygame.image.get_extended():
        raise RuntimeError("No extended image support")
    if not pygame.joystick.get_init():
        if not pygame.joystick.init():
            raise RuntimeError("Couldn't initialize joystick subsystem")
