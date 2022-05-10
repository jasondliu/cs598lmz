import ctypes
# Test ctypes.CField.

import sys
import ctypes
from ctypes import *

class X(Structure):
    _fields_ = [
        ("_length", c_int),
        ("_data", c_char * 4)
        ]

    def __repr__(self):
        return "X(%s)" % repr(self.data)

    def __str__(self):
        return self.data

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def data(self):
        return self._data[0:self.length]

    @data.setter
    def data(self, value):
        size = min(len(value), len(self._data))
        self._data[0:size] = value[0:size]
        self.length = size

X._fields_[1]._type_ = c_char * 4

x = X()
x.data = "Hello"
assert x.data == "Hell
