import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_char_p
    z = ctypes.c_ulong

s = S()
print s.x
s.x = 1
s.y = 'foo'
s.z = 1234
print s.x
print s.y
print s.z

print isinstance(s.x, ctypes.c_double)
