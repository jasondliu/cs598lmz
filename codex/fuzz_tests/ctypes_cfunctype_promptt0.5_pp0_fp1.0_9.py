import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def test(msg):
    print msg

CALLBACK = CFUNCTYPE(None, c_char_p)

# callback = CALLBACK(test)
callback = CALLBACK(lambda msg: print msg)
callback("hello world")
