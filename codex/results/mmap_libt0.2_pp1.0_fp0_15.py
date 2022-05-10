import mmap
import os
import sys
import time

from . import __version__
from . import config
from . import log
from . import util
from . import xdg
from . import xkb
from . import xlib
from . import xrandr
from . import xrecord
from . import xwindow

_log = log.get_logger()


class XKeyboard:
    """
    XKeyboard is a class that manages the keyboard state.

    It is responsible for:
    - managing the keyboard layout
    - managing the keyboard state
    - managing the keyboard LEDs
    - managing the keyboard rate and delay
    - managing the keyboard repeat
    - managing the keyboard autorepeat
    - managing the keyboard keymap
    - managing the keyboard keycodes
    - managing the keyboard keysyms
    - managing the keyboard modifiers
    - managing the keyboard groups
    - managing the keyboard group names
    - managing the keyboard group info
    - managing the keyboard group layouts
    - managing the keyboard group symbols
    - managing the keyboard group types
    - managing the keyboard group compat
    - managing the keyboard group geometry

