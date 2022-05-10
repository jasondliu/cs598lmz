import ctypes
# Test ctypes.CField
class A(ctypes.Structure):
    _fields_ = [("b", ctypes.CField)]
# CHECK-L: ctypes.CField
# CHECK-L-NEXT: Name: b
# CHECK-L-NEXT: Type: ctypes.CField
