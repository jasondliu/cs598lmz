import gc, weakref
from .lib import *
from . import modules
from . import environment
from . import tools
from . import config

# This is the main class of the game
class Game(object):
    def __init__(self, game_name = None, mode = None, screens = None, settings = None, 
                 commands = None, variables = None, actions = None, event_handler = None):
        # The name of the game
        self.name = game_name

        # The game's mode (single or multiplayer)
        self.mode = mode

        # A list of the screens in the game
        self.screens = screens

        # A list of the settings in the game
        self.settings = settings

        # A list of the commands in the game
        self.commands = commands

        # A list of the variables in the game
        self.variables = variables

        # A list of the actions in the game
        self.actions = actions

        # The event handler for the game
        self.event_handler = event_handler

    # This function creates the game
    def create(self,
