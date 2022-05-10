import ctypes
# Test ctypes.CField with struct
import ctypes

class C(ctypes.Structure):
    pass

class D(ctypes.Structure):
    pass

C._fields_ = [
    ('c_field', C),
    ('next', ctypes.POINTER(C)),
]

D._fields_ = [
    ('c_field', C),
    ('next', ctypes.POINTER(D)),
]
