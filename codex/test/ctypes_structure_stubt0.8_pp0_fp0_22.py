import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 2
    y = ctypes.c_char * 2

s = S()
s.x = b'\x00\x01'
s.y = b'\x01\x00'

print('%r' % s.x)
print('%r' % s.y)
print('%r' % s)
print('%r' % bytes(s))

