import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import time
from itertools import chain


from .MusicLibrary import Library
from .Track import Track
from .Album import Album
from .Artist import Artist
from .Playlist import Playlist
from .Genre import Genre
from .Song import Song
from .Utils import convert_time, mspf, get_win_unicode_console, write_unicode_to_console
from .Exceptions import *
from .Constants import *
from .Utils import *

# get the unicode console function
write_console = get_win_unicode_console()


class Winamp:
    """
    A class representing a single instance of Winamp. Currently only the first instance of the player is supported.
    """

    def __init__(self, force=False):
        """
        A constructor for a Winamp object.
        Raises NotRunning if Winamp is not running.
        :param force: Whether to force-initialize, even if Winamp is not running.
        """
        # initialize the library
        self.tracks = Library()

        # initialize the library
