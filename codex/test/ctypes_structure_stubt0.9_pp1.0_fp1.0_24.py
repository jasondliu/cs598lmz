import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()
    y = ctypes.c_long()

e = ctypes.c_void_p(-1)
i = ctypes.c_long(-1)
s = S(x=ctypes.c_long(-1), y=ctypes.c_long(-1))

print(repr(s))
print('e: %s, i: %s, s: %s' % (repr(e), repr(i), repr(s)))

