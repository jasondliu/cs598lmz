import ctypes

class S(ctypes.Structure):
    x = ctypes.c_byte(b'd')

class S2(ctypes.Structure):
    x = ctypes.c_byte(2)
    y = S

x = S2()
x.x += x.y.x
assert x.x == b'g'

# A simple test for module attributes that is cross-referenced from another
# module.

import example
assert example.demo.v == 4

example.demo.v += 1
assert example.demo.v == 5

assert example.mult(example.demo.v, exa
