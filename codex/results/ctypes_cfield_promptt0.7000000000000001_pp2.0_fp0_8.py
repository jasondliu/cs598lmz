import ctypes
# Test ctypes.CField
class SF(ctypes.Structure):
    _fields_ = [
        ('f1', ctypes.c_float),
        ('f2', ctypes.c_float),
    ]

class PF(ctypes.Structure):
    _fields_ = [
        ('f1', ctypes.POINTER(ctypes.c_float)),
        ('f2', ctypes.POINTER(ctypes.c_float)),
    ]

# Test that PF(pointer to float) can also be initialized from
# ctypes.py_object (which should be a python float).

a = SF(1, 2)
assert a.f1 == 1.0
assert a.f2 == 2.0

a = SF(1.5, 2.5)
assert a.f1 == 1.5
assert a.f2 == 2.5

pf = ctypes.pointer(a)
assert isinstance(pf.contents, SF)

a = PF(pf, pf)
assert a.f1 == pf
assert a.f2 == pf
