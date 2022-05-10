import ctypes
# Test ctypes.CField

# Simple field
class CTest1(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

# Long field
class CTest2(ctypes.Structure):
    _fields_ = [("a" * 500, ctypes.c_int)]

# Field containing spaces
class CTest3(ctypes.Structure):
    _fields_ = [("a b", ctypes.c_int)]

# Field containing forbidden characters
class CTest4(ctypes.Structure):
    _fields_ = [("a\0b", ctypes.c_int)]

# Field containing forbidden characters
class CTest5(ctypes.Structure):
    _fields_ = [("a\tb", ctypes.c_int)]

# Field containing forbidden characters
class CTest6(ctypes.Structure):
    _fields_ = [("a\rb", ctypes.c_int)]

# Field containing forbidden characters
class CTest7(ctypes.Structure):
    _fields_ = [("a\nb", ctypes
