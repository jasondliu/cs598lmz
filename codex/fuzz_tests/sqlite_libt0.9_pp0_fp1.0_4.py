import ctypes
import ctypes.util
import threading
import sqlite3
import os


class BoardGame(object):
    """static class (one instance only) that stores the gameboard data and
    provides the game logic"""

    def __init__(self, on_gameboard_changed = None, name = "board", rows=None, cols=None):
        self._init_completed = False
        self._on_put = on_gameboard_changed
        self._board = np.zeros((rows, cols), dtype=np.int8)
        self._rows = rows
        self._cols = cols
        self._lock = threading.Lock()
        self._name = name
        self._init_completed = True

    def _emit_change(self):
        if self._on_put:
            self._on_put()

    def on_board_changed(self, callback):
        if not self._init_completed:
            raise(Exception("BoardGame object is not initialized"))
        if not callable(callback):
            raise(ValueError("Argument of on_board_changed cannot be empty"))
        self
