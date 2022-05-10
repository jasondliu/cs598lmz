import ctypes
# Test ctypes.CFUNCTYPE
import atexit

def f(n):
    print n

atexit.register(f, 99)
import ctypes.util

# Test ctypes.util.find_library
ctypes.util.find_library("m")

print "importing os"
import os
print "importing time"
import time
print "importing sys"
import sys

def f(n):
    print n

# Test atexit
atexit.register(f, 1)
atexit.register(f, 2)
atexit.register(f, 3)
# Test ctypes

def callback(n):
    print n,

CALLBACKFUNC = ctypes.CFUNCTYPE(None, ctypes.c_int)
callbackfunc = CALLBACKFUNC(callback)

libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.qsort.argtypes = (ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_void_
