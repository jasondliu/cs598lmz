import ctypes
import ctypes.util
import threading
import sqlite3

from operator import attrgetter
from spooks import spooks
from spooks import spook_types
from spooks import strfont
from spooks import exception


try:
    _libc = ctypes.CDLL(ctypes.util.find_library("c"))
except OSError:  # pragma: no cover
    _libc = ctypes.CDLL(ctypes.util.find_library("msvcrt"))


_BACKSPACE = b"\x7f"
_CARRIAGE = b"\r"


class TerminalCurses(object):
    """Terminal that wraps curses."""

    _lock = None
    _screen = None

    def __init__(self, rows, columns):
        self.init()
        self.rows = rows
        self.columns = columns

        self._cursor_row = None
        self._cursor_column = None

    @property
    def height(self):
        """Height."""
        return self._screen.getmaxyx()[0]

