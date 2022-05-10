import ctypes
# Test ctypes.CField

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

s = S()
s.x = ctypes.c_int(42)
print(s.x)

# Test ctypes.CField in subclasses

class S_(S):
    _fields_ = [('y', ctypes.CField)]

s = S_()
s.x = ctypes.c_int(42)
s.y = ctypes.c_int(43)
print(s.x)
print(s.y)

# Test ctypes.CField in subclasses with __slots__

class S_S(S):
    __slots__ = ['y']
    _fields_ = [('y', ctypes.CField)]

s = S_S()
s.x = ctypes.c_int(42)
s.y = ctypes.c_int(43)
print(s.x)
print(s.y)

# Test ctypes.CField in subclasses with __slots
