import ctypes
ctypes.cast(p_b, ctypes.py_object).value

type(p_b)

p_b.contents
p_b.contents.value

#structures

from ctypes import *

class POINT(Structure):
    _fields_ = [
        ("x", c_int),
        ("y", c_int)
    ]

p = POINT()
p.x = 3
p.y = 4
print(p.x, p.y)
