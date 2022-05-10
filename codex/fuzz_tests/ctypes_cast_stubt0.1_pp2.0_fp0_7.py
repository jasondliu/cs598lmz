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

if sys.version_info[0] == 2 and sys.version_info[1] == 1:
    warnings.warn("Python 2.1 is no longer supported. "
                  "Please upgrade to a newer version (Python 2.3 or greater).")

# SOURCE LINE 18

if sys.version_info[0] == 2 and sys.version_info[1] == 2:
    warnings.warn("Python 2.2 is no longer supported. "
                  "Please upgrade to a newer version (Python 2.3 or greater).")

# SOURCE LINE 23

if sys.version_info[0] == 2 and sys.version_info[1] == 3:
    warnings.warn("Python 2.3 is no longer supported. "
                  "Please upgrade to a newer version (Python 2.4 or greater
