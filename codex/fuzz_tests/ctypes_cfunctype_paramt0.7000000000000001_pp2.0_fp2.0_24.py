import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def fun(x):
    return x**2

CFUN = FUNTYPE(fun)
CFUN(3)

# Example 2

from ctypes import *

libc = cdll.LoadLibrary('/usr/lib/libc.dylib')
libc.printf(b'hello, world')
# 6

# Example 3

from ctypes import *

libc = cdll.LoadLibrary('/usr/lib/libc.dylib')
libc.printf(b'%s\n', b'hello, world')
# hello, world
# 13

# Example 4

from ctypes import *

libc = cdll.LoadLibrary('/usr/lib/libc.dylib')
libc.printf(b'%s\n', b'hello, world', b'extra arg')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ArgumentError: argument 1: <class 'TypeError'>: wrong type

# Example
