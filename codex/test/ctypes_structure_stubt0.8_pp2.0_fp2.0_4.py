import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p()

def f(s):
    s.x = ctypes.c_char_p(b"abc")

s = S()
f(s)
print(s.x)
s.x = ctypes.c_char_p(b"def")
print(s.x)
