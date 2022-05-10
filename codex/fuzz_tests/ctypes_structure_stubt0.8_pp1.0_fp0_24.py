import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

assert S.x.offset == 0
assert S.y.offset == ctypes.sizeof(ctypes.c_int)

if sys.platform == "win32":
    assert S.y.offset == 4

assert S.x.size == ctypes.sizeof(ctypes.c_int)
assert S.y.size == ctypes.sizeof(ctypes.c_int)

s = S()
assert s.x == 0
assert s.y == 0

s.x = 42
assert s.x == 42
s.y = 42
assert s.y == 42

# test pack_into
from ctypes import Structure, c_int, sizeof
import array

class S(Structure):
    _pack_ = 1
    _fields_ = [("f1", c_int),
                ("f2", c_int),
                ("f3", c_int)]

buf = array.array("b", [0] * sizeof(S))
addr, offset =
