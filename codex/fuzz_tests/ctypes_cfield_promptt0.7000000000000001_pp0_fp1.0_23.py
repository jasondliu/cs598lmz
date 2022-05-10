import ctypes
# Test ctypes.CField

# These are all equivalent.

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ctypes.CField("c")]

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    c = ctypes.CField()

# CField instances have no name.
assert C.c.name == ""

# A structure can't have two fields with the same name:
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ctypes.CField("a"),
                ctypes.CField("b")]

