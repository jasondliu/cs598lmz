import ctypes
# Test ctypes.CFields
class x(ctypes.Structure):
    pass

class y(ctypes.Structure):
    _fields_ = (('a', x))

class z(ctypes.Structure):
    _fields_ = (('b', y))

z()
