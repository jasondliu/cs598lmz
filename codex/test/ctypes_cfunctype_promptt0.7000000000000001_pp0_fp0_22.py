import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *

def func(*args):
    print(args)

ctypes.CFUNCTYPE(None, c_int, c_int)(func)

def func(*args):
    print(len(args))

ctypes.CFUNCTYPE(None, c_int, c_int)(func)

def func(*args):
    print(args)

ctypes.CFUNCTYPE(None)(func)

def func(*args):
    print(len(args))

ctypes.CFUNCTYPE(None)(func)

def func(*args):
    print(args)

ctypes.CFUNCTYPE(c_int, c_int, c_int)(func)

def func(*args):
    print(len(args))

ctypes.CFUNCTYPE(c_int, c_int, c_int)(func)

def func(*args):
    print(args)

ctypes.CFUNCTYPE(c_int)(func)

