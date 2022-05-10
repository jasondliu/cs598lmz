import ctypes
# Test ctypes.CField with a structure. Bug #9172 compatible with pypy.
class S(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

s = S()

s.x = 5
try:
    s.x = 0xdeadbeef
except OverflowError:
    pass
else:
    raise RuntimeError("should raise OverflowError when assigning 32 bits to a signed int field")

s.x = 13
try:
    s.x = 0x4200000000000000
except OverflowError:
    pass
else:
    raise RuntimeError("should raise OverflowError when assigning a signed 64 bits to a signed int field")

class U(ctypes.Union):
    _fields_ = [('u', ctypes.CField)]

u = U()
u.u = 0xdeadbeef
assert u.u == 0xdeadbeef
try:
    u.u = 1.25
except TypeError:
    pass
else:
    raise RuntimeError("should not celebrate")

# Pushing this test further.  If you want
