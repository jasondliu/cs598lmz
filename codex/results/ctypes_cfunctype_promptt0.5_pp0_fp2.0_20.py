import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *

def func(x):
    return x + 1

f = CFUNCTYPE(c_int, c_int)(func)
print f(3)

try:
    f = CFUNCTYPE(c_int, c_int)(lambda x: x + 1)
    print f(3)
except TypeError, e:
    print e

try:
    f = CFUNCTYPE(c_int, c_int)(lambda x, y: x + y)
    print f(3)
except TypeError, e:
    print e

try:
    f = CFUNCTYPE(c_int, c_int)(lambda x: x + 1, x = 3)
    print f()
except TypeError, e:
    print e

try:
    f = CFUNCTYPE(c_int, c_int)(lambda x: x + 1, x = 3, y = 4)
    print f()
except TypeError, e:
    print e

try:
    f = CFUNCTY
