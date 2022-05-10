import ctypes
# Test ctypes.CFUNCTYPE with several function types
from ctypes import *
from ctypes.test import is_resource_enabled

class X(Structure):
    _fields_ = [("x", c_int)]

class Y(Structure):
    _fields_ = [("y", c_int)]

def callback(*args):
    pass

# define the prototypes
PROTOTYPES = (c_char_p,
              c_int,
              c_char_p,
              c_int,
              POINTER(c_char),
              c_char_p,
              c_int,
              POINTER(X),
              c_char_p,
              c_int,
              POINTER(Y),
              POINTER(c_int),
              #POINTER(POINTER(c_char)),
              c_char_p,
              c_char_p,
              c_int,
              )

if is_resource_enabled("printing"):
    import traceback
    import sys

    # Our own excepthook, looks a bit like the one used by p
