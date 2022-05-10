import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import os
import sys
import time
import logging
import threading
import traceback
import warnings

# SOURCE LINE 11

import pygame

# SOURCE LINE 13

from pygame.compat import geterror
from pygame.constants import *
from pygame.version import ver

# SOURCE LINE 17

from pygame.base import *
from pygame.base import _PYGAMEinit_GFX_PYGAMEinit as _PYGAMEinit
from pygame.base import _PYGAME_C_API

# SOURCE LINE 21

from pygame.rect import Rect
from pygame.surface import Surface
from pygame.display import set_mode, get_surface, get_init, Info, \
     list_modes, mode_ok, set_caption, set_icon, get_caption, \
     set_palette, set_gamma, set_gamma_ramp, get_gamma_ramp, \
     get_active, flip, update,
