import select
import sys
import time

import pygame

from . import config
from . import constants
from . import control
from . import display
from . import events
from . import game
from . import graphics
from . import input
from . import resources
from . import sound
from . import state
from . import text
from . import ui
from . import util
from . import world

from . import __version__


class Engine:
    """The game engine.

    This class manages the game loop, and is responsible for loading
    and initializing the various game components.

    """

    def __init__(self):
        """Initialize the engine."""
