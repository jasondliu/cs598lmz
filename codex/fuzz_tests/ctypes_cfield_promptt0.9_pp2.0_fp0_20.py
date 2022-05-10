import ctypes
# Test ctypes.CField by using the field setter
# as a parameter.
import sys
from ctypes import Structure, Field

class POINT(Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int)
        ]

x = POINT()
x.x = 1
x.y = 2

class Line(Structure):
    _opaque_ = True
    dot = POINT
    _fields_ = [ ("start", dot),
                 ("end", dot) ]

# This fails miserably on current py3k, as the function
# object is converted to a str
obj = Line.start
Line.create([["x", obj]])

# This succeeds
Line.create([["x", ctypes.CFUNCTYPE(None, Line.start)],
             ["x", "y", ctypes.CFUNCTYPE(None, Line.start, Line.end)]])

if sys.version_info[0] != 3:
    # Using the field pointer as a type by using _type_ =
