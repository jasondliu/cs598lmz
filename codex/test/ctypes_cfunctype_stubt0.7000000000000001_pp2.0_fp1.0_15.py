import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hi'

fun.__dict__

@classmethod
def fun(cls, *args):
    return args

fun.__dict__

fun.__annotations__

from collections import namedtuple

Point = namedtuple('Point', 'x y')

p = Point(1, 2)
p.x
p.y

