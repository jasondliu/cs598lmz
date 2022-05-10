import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong(0x4242424242424242)
    y = ctypes.c_longlong(0x4141414141414141)

print id(S.x)
print id(S.y)

s = S()
print s.x.__dict__
print s.y.__dict__
print s.__dict__
