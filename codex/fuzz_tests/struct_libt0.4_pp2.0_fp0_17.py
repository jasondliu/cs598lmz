import _struct
import ctypes
import ctypes.util
import errno
import fcntl
import os
import select
import socket
import sys
import termios
import textwrap
import traceback

import pyte
import pyte.graphics

from . import ansi
from . import compat
from . import errors
from . import fdwrap
from . import io
from . import keys
from . import log
from . import loop
from . import mouse
from . import screen
from . import selection
from . import terminal
from . import utils
from . import window
from .log import logger
from .screen import Screen
from .terminal import Terminal
from .window import Window


class Display:
    """
    A high-level API for creating terminals and windows.

    This is a convenience wrapper around the low-level API.
    """

    def __init__(self, term=None, term_size=None,
                 palette=None, font=None,
                 dpi=96, spacing=0,
                 cursor_blink=False,
                 cursor_shape=None,
                 mouse_
