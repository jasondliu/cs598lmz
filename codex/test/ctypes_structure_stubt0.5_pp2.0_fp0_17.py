import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

S_p = ctypes.POINTER(S)

def f(x, y):
    return x+y

f_p = ctypes.CFUNCTYPE(ctypes.c_int, S_p, S_p)(f)

s1 = S()
s2 = S()

s1.x = 1
s1.y = 2
s2.x = 3
s2.y = 4

print(f_p(s1, s2))
