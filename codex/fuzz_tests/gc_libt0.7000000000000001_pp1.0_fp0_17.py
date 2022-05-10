import gc, weakref
import sys

# This module is the real main module of the game, but we import it as game
# This is because we want to be able to run the game from a different module
# without it closing when the game exits.
# This way we can run the game from the editor, and it will not close
# when we open the game.

import game

# Import our own modules
import resources
import state
import eztext
import entity
import aspect
import direction
import events
import world
import message

# Import the logging module
import logging

# Define the logger
logger = logging.getLogger(__name__)

# Create a weak reference to this object so that we can access it from
# other modules.
# This is used by the editor module to send events to the game
# TODO: Should use a proper event system
# TODO: Should use a different approach to get reference to game
# TODO: Should avoid referencing the game object at all
game_ref = weakref.ref(None)

# Create a dictionary of the states in the game
states = {}

#
