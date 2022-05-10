import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("value", ctypes.c_int),
                ("name", ctypes.CField)]
    def __init__(self):
        self.value = 2
        self.name = "Hello"

x = X()
print x.value, x.name

import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("value", ctypes.c_int),
                ("name", ctypes.CField)]
    def __init__(self):
        self.value = 2
        self.name = "Hello"

x = X()
print x.value, x.name

# Train on the ctype module
# What are the differences between a ctype string and a ctype wstring?
import ctypes
print ctypes.c_char_p()
print ctypes.c_wchar_p()

# Can you make an instance of a ctype array?
import ctypes
# This works:
print ctypes.c_char_p
