import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

# Create some functions

def func(x):
    return x*5

def func_var(x, y):
    return x*y

