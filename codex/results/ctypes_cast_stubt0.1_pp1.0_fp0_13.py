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

if sys.version_info[0] == 2 and sys.version_info[1] <= 4:
    from sets import Set as set

# SOURCE LINE 17

from pygame.base import *
from pygame.constants import *
from pygame.version import ver

# SOURCE LINE 21

from pygame.rect import Rect
from pygame.surface import Surface
from pygame.color import Color
from pygame.locals import *
from pygame.sprite import Sprite, Group, RenderUpdates
from pygame.event import Event, EventType
from pygame.time import Clock, get_ticks, delay, wait
from pygame.font import Font, SysFont, get_fonts, match_font
from pygame.image import load, save, get_extended, get_
