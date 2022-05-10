import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p

s = S()

# default
S.x.__ctype_le__ = None
s.x = s
print('s.x:  ', repr(s.x))

# big-endian
S.x.__ctype_le__ = False
s.x = s
print('s.x:  ', repr(s.x))

# little-endian
S.x.__ctype_le__ = True
s.x = s
print('s.x:  ', repr(s.x))
