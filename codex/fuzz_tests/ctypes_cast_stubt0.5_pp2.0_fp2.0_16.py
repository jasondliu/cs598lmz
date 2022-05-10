import ctypes
ctypes.cast(0, ctypes.py_object)

import sys
from ctypes.util import find_library

from ctypes import *

if sys.platform == "win32":
    _lib = CDLL(find_library("SDL2"))
else:
    _lib = CDLL("libSDL2.so")

# SDL_INIT_TIMER          = 0x00000001
# SDL_INIT_AUDIO          = 0x00000010
# SDL_INIT_VIDEO          = 0x00000020
# SDL_INIT_JOYSTICK       = 0x00000200
# SDL_INIT_HAPTIC         = 0x00001000
# SDL_INIT_GAMECONTROLLER = 0x00002000
# SDL_INIT_EVENTS         = 0x00004000
# SDL_INIT_NOPARACHUTE    = 0x00100000
# SDL_INIT_EVERYTHING     = SDL_INIT_TIMER | SDL_INIT_AUDIO | SDL_INIT_VIDEO | SDL_INIT_EVENTS | SDL
