import ctypes
# Test ctypes.CFUNCTYPE() argument and return types.
from array import array
import _ctypes_test

try:
    unicode
except NameError:
    unicode = str

if os.name == "nt":
    from _ctypes import FreeLibrary as dll_unload
else:
    from _ctypes import dlclose as dll_unload

################################################################
#
# some callback functions

def callback(*args):
    global called
    called = True
    if len(args) == 1:
        return args[0] * 2
    else:
        return args[0] * args[1] * 2

def callback_l(*args):
    global called
    called = True
    if len(args) == 1:
        return ctypes.c_long(args[0] * 2).value
    else:
        return ctypes.c_long(args[0] * args[1] * 2).value

def callback_ll(*args):
    global called
    called = True
    if len(args) == 1:
        return ctypes.c_long
