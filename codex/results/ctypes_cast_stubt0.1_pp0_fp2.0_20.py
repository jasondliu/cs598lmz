import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import os
import sys
import time
import threading
import traceback
import warnings

# SOURCE LINE 10

import pygame
from pygame.compat import geterror

# SOURCE LINE 13

if sys.version_info[0] == 2 and sys.version_info[1] < 6:
    raise SystemExit("Python 2.6 or greater is required to run pygame")

# SOURCE LINE 17

if sys.version_info[0] == 3:
    import builtins
else:
    import __builtin__ as builtins

# SOURCE LINE 22

import pygame.base
from pygame.base import *

# SOURCE LINE 25

from pygame.version import ver as __version__

# SOURCE LINE 27

from pygame.version import sdl_version as __sdl_version__

# SOURCE LINE 29

from pygame.version import sdl_rev as __sdl_rev__

# SOURCE LINE 31

from pygame
