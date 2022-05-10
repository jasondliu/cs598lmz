import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is for the case where the function pointer is passed as an
# argument to another function.
#
# The function pointer is created using ctypes.CFUNCTYPE.  The function
# pointer is passed as an argument to another function.  The function
# pointer is called from the other function.
#
# This test is for the case where the function pointer is passed as an
# argument to another function.

# This test is for the case where the function pointer is passed as an
# argument to another function.

import ctypes
from ctypes import *

# /home/user/PycharmProjects/untitled/venv/include/SDL2/SDL_video.h: 518
for _lib in _libs.values():
    if not hasattr(_lib, 'SDL_SetWindowHitTest'):
        continue
    SDL_SetWindowHitTest = _lib.SDL_SetWindowHitTest
    SDL_SetWindowHitTest.argtypes = [POINTER(SDL_Window), CFUNCTYPE(ctypes.c_int, POINTER
