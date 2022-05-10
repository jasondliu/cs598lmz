import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(*args):
    print(args)

CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(func)(1, 2)

################################################################
#
#  $ python test_cfunctype.py
#  (1, 2)
#
