import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 3

import os
import sys
import warnings
import traceback

# SOURCE LINE 8

import pygame
from pygame.compat import geterror

# SOURCE LINE 11

if sys.version_info[0] >= 3:
    import builtins
else:
    import __builtin__ as builtins

# SOURCE LINE 16

if sys.platform == 'win32' or sys.platform == 'win64':
    os.environ['SDL_VIDEODRIVER'] = 'windib'

# SOURCE LINE 20

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'data')

# SOURCE LINE 24

def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
