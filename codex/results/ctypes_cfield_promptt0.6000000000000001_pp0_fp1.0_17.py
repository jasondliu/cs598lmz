import ctypes
# Test ctypes.CField

class test:
    def __init__(self, data):
        self.data = data

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int),
                ("e", ctypes.c_int),
                ("f", ctypes.c_int)]

x = X()
x.a = 1
x.b = 2
x.c = 3
x.d = 4

# A CField is a pointer to a field, of the same type as the field.
# For example, if x.a is an int, then x.a.contents is an int pointer.
# Changing the value
