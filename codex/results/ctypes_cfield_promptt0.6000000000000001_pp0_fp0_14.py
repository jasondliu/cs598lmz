import ctypes
# Test ctypes.CField()

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int)]

    _anonymous_ = ["_"]
    _fields_ = [("_", POINT * 3),
                ("name", ctypes.c_char * 16)]

p = POINT()
p.x = 1
p.name = "hello"

import pprint
pprint.pprint(p._objects)
print p.name
