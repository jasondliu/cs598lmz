import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import os
import sys
import time
import threading
import traceback
import warnings

# SOURCE LINE 11

import pygame
from pygame.compat import geterror

# SOURCE LINE 14

if sys.version_info[0] == 2 and sys.version_info[1] == 1:
    warnings.warn("Python 2.1 is no longer supported by Pygame. "
                  "Please upgrade to a newer version.")

# SOURCE LINE 19

if sys.version_info[0] == 2 and sys.version_info[1] == 2:
    warnings.warn("Python 2.2 is no longer supported by Pygame. "
                  "Please upgrade to a newer version.")

# SOURCE LINE 24

if sys.version_info[0] == 2 and sys.version_info[1] == 3:
    warnings.warn("Python 2.3 is no longer supported by Pygame. "
                  "Please upgrade to a newer version.")

# SOURCE LINE 29

if sys.version
