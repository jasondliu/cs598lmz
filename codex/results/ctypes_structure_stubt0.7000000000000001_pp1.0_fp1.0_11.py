import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

p = ctypes.pointer(S())
p.contents.x = 42
p.contents.y = 24
assert p.contents.x == 42
assert p.contents.y == 24

p.contents = S()
assert p.contents.x == 0
assert p.contents.y == 0

try:
    p.contents = "hello world"
except TypeError:
    pass
else:
    raise Exception("TypeError expected")

p.contents = S(1, 2)
assert p.contents.x == 1
assert p.contents.y == 2
