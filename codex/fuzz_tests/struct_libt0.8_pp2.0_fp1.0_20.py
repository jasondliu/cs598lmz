import _struct
from _md5 import md5

from base64 import b64decode
from base64 import b64encode
from itertools import izip
from math import ceil
from math import pow
from time import time


class Connect4(object):
    '''
    The class where most of the game logic resides.
    '''
    # The possible states that a game can be in.
    PLAYING = 0
    GAME_WON = 1
    DRAW = 2

    # The possible marks that a player can have.
    PLAYER_RED = 0
    PLAYER_YELLOW = 1
    PLAYER_NONE = 2

    def __init__(self, rows=6, cols=7):
        '''
        Initializes an instance of the Connect4 class.

        Args:
            rows: The number of rows in the game.
            cols: The number of columns in the game.
        '''
        self.rows = rows
        self.cols = cols
        self._state = Connect4.PLAYING
        self._init_board()
