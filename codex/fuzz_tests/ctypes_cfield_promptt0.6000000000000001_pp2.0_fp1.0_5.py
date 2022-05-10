import ctypes
# Test ctypes.CField.from_address
#
# This test is not part of the test suite, because it depends on the
# address  of some variable, so it can't be run in isolation.

# Run this by hand to verify that the result is correct.

import ctypes

# This variable must be in the range 0x1000-0x2000
var = 0x1000

p = ctypes.c_void_p.from_address(var)

class S(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int),
                ('d', ctypes.c_int),
               ]

s = S.from_address(var)
print(s.a)
print(s.b)
print(s.c)
print(s.d)
