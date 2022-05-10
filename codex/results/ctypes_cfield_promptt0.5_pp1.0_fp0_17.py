import ctypes
# Test ctypes.CField.

# This test is run by test_ctypes.py and is not meant to be run by itself.

# Create a ctypes instance of a structure to test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]

x = X()

# ctypes.CField has the following methods:
# __get__(self, instance, owner)
# __set__(self, instance, value)
# from_param(self, instance)

# Test __get__

assert ctypes.CField.__get__(X._fields_[0], x, X) == 0
assert ctypes.CField.__get__(X._fields_[1], x, X) == 0

# Test __set__

ctypes.CField.__set__(X._fields_[0], x, 42)
assert ctypes.CField.__get__(X._fields_[0], x, X) == 42

ctypes.CField.__
