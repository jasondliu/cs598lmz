import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

def func(x):
    return x + 1

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

cb = CALLBACK(func)

print cb(1)

# Test ctypes.Structure

import ctypes

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

p = Point()
p.x = 1
p.y = 2

print p.x
print p.y

# Test ctypes.Union

import ctypes

class Point(ctypes.Union):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

p = Point()
p.x = 1

print p.x
print p.y

# Test ctypes.POINTER

import ctypes

class Point(ctypes.Structure):
    _fields_ = [('
