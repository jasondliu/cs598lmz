import ctypes
# Test ctypes.CFUNCTYPE, with prototypes for some functions from
# the C library, to test the 'restype' and 'argtypes' attributes.
from ctypes import *
from ctypes.test import need_symbol

################################################################
#
# Some C library functions

need_symbol('strlen')
if hasattr(ctypes, 'set_conversion_mode'):
    ctypes.set_conversion_mode("ascii", "strict")

strlen = cdll.msvcrt.strlen
strlen.argtypes = c_char_p,
strlen.restype = c_size_t

strcpy = cdll.msvcrt.strcpy
strcpy.argtypes = c_char_p, c_char_p
strcpy.restype = c_char_p

strcat = cdll.msvcrt.strcat
strcat.argtypes = c_char_p, c_char_p
strcat.restype = c_char_p

atol = cdll.msvcrt.atol
atol
