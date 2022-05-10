import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    pass
f1 = ctypes.CField(ctypes.c_int, 33)
f2 = ctypes.CField(ctypes.c_int, 66)
f3 = ctypes.CField(ctypes.c_int, 99)
f1.offset = 12
f2.offset = 16
f3.offset = 22
assert f1.offset == 12
assert f2.offset == 16
assert f3.offset == 22
C._fields_ = [f1, f2, f3]
assert f1.offset == 0
assert f2.offset == 4
assert f3.offset == 8
p = C()
assert p.i1 == 33
assert p.i2 == 66
assert p.i3 == 99
assert p._objects == None
assert p._b_needsfree_ == 0
assert p._b_needsfree_ == 0
assert p._length_ == 12
assert p._sizeofinstances() == 12
try:
    p.i1 = 42
    raise Exception("shouldn't get here")
except
