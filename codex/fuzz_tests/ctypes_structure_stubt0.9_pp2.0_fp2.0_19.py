import ctypes

class S(ctypes.Structure):
    x = 8
    _fields_ = [('y', ctypes.c_long) ]
    _packed_ = True

size = ctypes.sizeof(S)
assert size == ctypes.c_long().size

s = S()
s.x = 0x08070605
s.y = 0x04030201
assert s.x == 0x05060708
assert s.y == 0x01020304

# from issue #3016
from ctypes import *
from ctypes.wintypes import *

# This (HHOKNOTIFYPROC) is the real type, with a callback and a
# HWND. Using a custom callback to make the test simpler.
HHOKNOTIFYPROC = WINFUNCTYPE(None, HWND, c_int, HWND, c_int, c_int32, c_void_p)

class HH_AKLINK(Structure):
    _fields_ = [ ('cbStruct', c_int), ('fReserved', c_int),
                 ('curKey', c_int), ('pszKeywords', c
