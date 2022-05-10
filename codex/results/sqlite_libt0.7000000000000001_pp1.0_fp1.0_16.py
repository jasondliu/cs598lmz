import ctypes
import ctypes.util
import threading
import sqlite3
import math

import pyglet

import ppb

#
# This is a utility function to find the game's "resources" folder. We use this
# to load the music and sound files we need.
#
def find_res(path):
    """
    A utility function to find where our resources are located.
    """
    res = ctypes.util.find_library('resources')
    if res is not None:
        return os.path.join(res, path)
    else:
        return path

class Level(ppb.BaseScene):
    """
    The Level is the main scene for the game. It handles the player, powerups,
    and generally all of the action in the game.
    """
    def __init__(self, *args, **kwargs):
        """
        The Level constructor sets up the background music and the sound
        effects. We will also load the level from the database here.
        """
        super().__init__(*args, **kwargs)

        # Set up the database connection.
        self.db = sqlite3.connect
