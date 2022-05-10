import ctypes
# Test ctypes.CField
class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
    _anonymous_ = ("a",)

# Test ctypes.c_void_p
class B(ctypes.Structure):
    _fields_ = [("b", ctypes.c_void_p)]
    _anonymous_ = ("b",)

# Test ctypes.c_char_p
class C(ctypes.Structure):
    _fields_ = [("c", ctypes.c_char_p)]
    _anonymous_ = ("c",)

# Test ctypes.c_wchar_p
class D(ctypes.Structure):
    _fields_ = [("d", ctypes.c_wchar_p)]
    _anonymous_ = ("d",)

# Test ctypes.c_ubyte
class E(ctypes.Structure):
    _fields_ = [("e", ctypes.c_ubyte)]
    _anonymous_ = ("e",)

# Test ctypes.c
