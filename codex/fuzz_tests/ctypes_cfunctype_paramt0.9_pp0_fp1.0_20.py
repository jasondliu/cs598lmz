import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

from pygame2.win32 import (ctypes_wintypes, winkeycodes, _is_winkey,
                           _is_winkey_extended)
from pygame2.sdl.events import SDL_EVENTMASK, SDL_KEYDOWN, SDL_KEYUP
from pygame2.sdl import dll
from pygame2.sdl.error import SDLError


_GetAsyncKeyState = dll.windll.user32.GetAsyncKeyState
_GetAsyncKeyState.argtypes = (ctypes_wintypes.WORD,)
_GetAsyncKeyState.restype = (ctypes_wintypes.SHORT,)

_GetKeyboardState = dll.windll.user32.GetKeyboardState
_GetKeyboardState.argtypes = (ctypes.POINTER(ctypes_wintypes.BYTE),)
_GetKeyboardState.restype = (ctypes_wintypes.BOOL,)

_ToUnicode = dll.windll.user32.ToUnicode
_ToUnicode
