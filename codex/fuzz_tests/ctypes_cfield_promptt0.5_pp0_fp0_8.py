import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
# Test ctypes.Structure
class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
# Test ctypes.Union
class E(ctypes.Union):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
# Test ctypes.Array
class F(ctypes.Array):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
# Test ctypes.Pointer
class G(ctypes.Pointer):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
# Test ctypes.CFuncPtr
class H(ctypes.CFuncPtr):
    _fields_ = [("a", ctypes.
