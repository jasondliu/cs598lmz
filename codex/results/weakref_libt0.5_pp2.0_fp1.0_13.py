import weakref

from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse

from . import util
from . import resources
from . import graphics
from . import particle
from . import physics
from . import ui
from . import world
from . import camera

class Game(object):
    """
    The main game object.  This class is responsible for managing the state
    of the game, and routing input events to the appropriate handlers.
    """

    def __init__(self, window, level):
        """
        Initialize the game object.  This function is called when the game
        is first created.

        :Parameters:
            `window` : `pyglet.window.Window`
                The window in which the game will be played.
            `level` : `game.world.Level`
                The level to load into the game.
        """
        self.window = window
        self.window.push_handlers(self)
        self.level = level

        # A list of handlers for input events.  When an event occurs, it
