import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def func(a, b):
    print a, b
    return -1

CFUNCTYPE(c_int, c_int, c_int)(func)(1, 2)

f = CFUNCTYPE(c_int, c_int, c_int)(func)
f(5, 6)

CFUNCTYPE(c_int, c_int, c_int)(None)

class Foo(object):
    def func(self, a):
        print a
        return -1

CFUNCTYPE(c_int, c_int)(Foo().func)

f = CFUNCTYPE(c_int, c_int)(Foo().func)
f(7)

CFUNCTYPE(c_int, c_int)(Foo().func)

# ctypes.CFUNCTYPE with bound methods

# Test passing the address of a ctypes data type
# as the first argument to a ctypes callback

# Test calling a ctypes callback from a different thread
import thread
