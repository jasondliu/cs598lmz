import ctypes
# Test ctypes.CFields

import os
from ctypes import *

class X(Structure):
    _fields_ = [
        ("next", POINTER(X)),
        ("value", c_int),
    ]

p = pointer(X(None, 42))

if sizeof(p.contents) != sizeof(X):
    raise Exception("sizeof(p.contents) != sizeof(X)")
if p.contents.value != 42:
    raise Exception("p.contents.value != 42")

# Test ctypes.CFields.from_param

class X:
    def __init__(self, value):
        self.value = value
    def _as_parameter_(self):
        return self.value

class Y(Structure):
    _fields_ = [
        ("next", POINTER(Y)),
        ("value", c_int),
    ]

p = pointer(Y(None, X(42)))
if p.contents.value != 42:
    raise Exception("p.contents.value != 42")

# Test ctypes.
