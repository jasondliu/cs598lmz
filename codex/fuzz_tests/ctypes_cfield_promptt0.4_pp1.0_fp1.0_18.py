import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.CField)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.CField)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.CField)]

# Test ctypes.CFuncPtr
class A(ctypes.Structure):
    _fields_ = [("a", ctypes.CFuncPtr)]

class B(ctypes.Structure):
    _fields_ = [("a", ctypes.CFuncPtr)]

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.CFuncPtr)]

# Test ctypes.CPointer
class D(ctypes.Structure):
    _fields_ = [("a", ctypes.CPointer)]

class E(ctypes.Structure):
    _fields_ = [("a", ctypes.CPointer)]

class F(ctypes.Structure):
    _fields_ = [
