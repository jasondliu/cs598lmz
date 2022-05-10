import ctypes
# Test ctypes.CField()

# Derive objects from Structure and make fields of type ctypes.CField()

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.CField()), ("b", ctypes.CField())]

class Y(ctypes.Structure):
    _fields_ = [("x", X), ("c", ctypes.CField())]

# ctypes.CField() can only be used as fields, not as elements of arrays
class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.CField() * 10)]

class W(ctypes.Structure):
    _fields_ = [("b", ctypes.CField() * (10, 10))]

class V(ctypes.Structure):
    _fields_ = [("c", ctypes.CField() * 10 * 10)]

class U(ctypes.Structure):
    _fields_ = [("a", ctypes.CField() * 10), ("b", ctypes.CField() * (10, 10))]

class
