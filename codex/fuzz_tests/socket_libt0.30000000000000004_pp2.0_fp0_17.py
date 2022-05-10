import socket
import sys
import threading
import time

import numpy as np
import pygame

from . import config
from . import constants
from . import controller
from . import display
from . import game
from . import game_state
from . import game_state_manager
from . import game_state_menu
from . import game_state_play
from . import game_state_score
from . import game_state_server
from . import game_state_settings
from . import game_state_splash
from . import game_state_waiting
from . import network
from . import player
from . import score
from . import sound
from . import sprite
from . import sprite_manager
from . import text
from . import util


class Game(object):
    """
    The main game class.
    """

    def __init__(self):
        """
        Initialize the game.
        """

        # Initialize the game.
        pygame.init()

        # Initialize the display.
        self.display = display.Display()

        # Initialize the sound.
       
