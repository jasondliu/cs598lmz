import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.CField),
        ('b', ctypes.CField)]

# Test ctypes.Field
class Y(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.Field),
        ('b', ctypes.Field)]

# Test ctypes.PYFUNCTYPE
class Z(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.PYFUNCTYPE),
        ('b', ctypes.PYFUNCTYPE)]

# Test ctypes.POINTER
class W(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.POINTER(ctypes.c_int)),
        ('b', ctypes.POINTER(ctypes.c_int))]

# Test ctypes.POINTER(ctypes.PYFUNCTYPE)
class V(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.POINTER(ct
