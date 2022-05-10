import ctypes
# Test ctypes.CFUNCTYPE
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)
f(1)

# Test ctypes.POINTER
p = ctypes.POINTER(ctypes.c_int)(ctypes.c_int(42))
p[0]

# Test ctypes.pointer
p = ctypes.pointer(ctypes.c_int(42))
p[0]

# Test ctypes.Structure
class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
s = S()
s.x = 42
s.x

# Test ctypes.Union
class U(ctypes.Union):
    _fields_ = [("x", ctypes.c_int)]
u = U()
u.x = 42
u.x

# Test ctypes.BigEndianStructure
class S(ctypes.BigEndianStructure):
    _fields_ = [("x", ctypes.c_int)]
s = S()
