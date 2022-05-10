import ctypes
# Test ctypes.CField.
# (ctypes.CField is only normally used by the metaclass CFields.)

class X(ctypes.Structure):
    pass
class P(ctypes.Structure):
    _fields_ = [
                ("x1", X),
                ("x2", X),
                ("x3", X),
                ("x4", X),
                ]
print P.x1
print P.x4
print P.x3
print P.x2
print type(P.x1)
print type(P.x2)
print type(P.x3)
print type(P.x4)
