import ctypes
# Test ctypes.CField class
from ctypes import Structure, Union


class C(Structure):
    _fields_ = [('allocated', ctypes.c_int)]
    def __init__(self):
        self.allocated = 1
        self.filled = 0
    def __repr__(self):
        return '<C instance: allocated=%d, filled=%d>' % (
            self.allocated, self.filled)
    def inc_filled(self):
        self.filled += 1

class CA(Structure):
    _fields_ = [('allocated', ctypes.c_int)]
    def __init__(self):
        self.allocated = 1
        self.filled = 0
        self.a = []
    def __repr__(self):
        return '<CA instance: allocated=%d, filled=%d, a=%r>' % (
            self.allocated, self.filled, self.a)
    def inc_filled(self):
        self.filled += 1

class CB(C):
    _fields_ = [('
