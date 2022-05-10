import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p
    y = ctypes.c_char_p

s = S()
print(s)
s.x = 'abc'
s.y = '123'

p = ctypes.pointer(s)
print(ctypes.cast(p, ctypes.c_void_p).value)
pp = ctypes.cast(p, ctypes.c_void_p).value
print(ctypes.cast(pp, ctypes.POINTER(S)).contents.x)
