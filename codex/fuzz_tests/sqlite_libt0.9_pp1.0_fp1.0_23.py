import ctypes
import ctypes.util
import threading
import sqlite3

from .struct import *


class PygletError(Exception):
    """Generic error raised on any program failure."""


class RaiseException(Exception):
    """Raise this exception to stop event dispatch and raise an exception.

    This is used to participate in python's exception handling "across the
    gap" with pyglet's event handlers.
    """

    def __init__(self, exc_type, exc_value, exc_traceback):
        self.exc_info = (exc_type, exc_value, exc_traceback)


def fail_on_error(func):
    def fail_on_error_method(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        if result != self._NO_ERROR:
            error_message = self.last_error
            if not error_message:
                error_message = 'Error code: %d' % result
            raise PygletError(error_message)
        return result

    return fail_on_error_method


def load_library():
    if
