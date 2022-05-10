import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                (ctypes.CField, ctypes.c_int),
                ("b", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                (ctypes.CField * 2, ctypes.c_int),
                ("b", ctypes.c_int)]

# This should fail:
try:
    class A(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int),
                    (ctypes.CField * 2, ctypes.c_int),
                    ("b", ctypes.c_int),
                    ("c", ctypes.c_int)]
except TypeError:
    pass
else:
    print "shouldn't get here"

