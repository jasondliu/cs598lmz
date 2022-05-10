import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p(b'foo')
    y = ctypes.c_char_p(b'bar')

s = S()
print(s.x)
print(s.y)
print(s.x.value)
print(s.y.value)
