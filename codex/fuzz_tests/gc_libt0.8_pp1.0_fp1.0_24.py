import gc, weakref, inspect

from .enums import *
from .defs import *
from .types import *
from .window import *
from .util import *

import pyglet

class Mouse(object):
    """Wrapper for mouse-related functions of the renderer."""

    def __init__(self, host):
        self._host = host

    def set_cursor(self, cursor_id, object=None):
        """Sets the global mouse cursor for the renderer.

        The cursor ID can be one of the following:
          - `CR_ARROW`: Standard arrow cursor.
          - `CR_IBEAM`: Text edit cursor.
          - `CR_CROSS`: Cross cursor.
          - `CR_POINTING_HAND`: Pointer cursor.
          - `CR_RESIZE_LEFT_RIGHT`: Left-right resize cursor.
          - `CR_RESIZE_UP_DOWN`: Up-down resize cursor.
          - `CR_RESIZE_TOP_LEFT_BOTTOM_RIGHT`: Diagonal resize cursor

