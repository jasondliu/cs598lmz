import ctypes

class S(ctypes.Structure):
    x = ctypes.c_short
    y = ctypes.c_short
    z = ctypes.c_short

def f():
    s1 = S()
    s1.x = 1
    s1.y = 2
    s1.z = 3
    s2 = S()
    s2.x = 4
    s2.y = 5
    s2.z = 6
    return s1, s2

s1, s2 = f()
print(s1.x, s1.y, s1.z)
print(s2.x, s2.y, s2.z)
