import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

def f():
    s = S()
    s.x = 1
    s.y = 2
    return s

print(f().x)
print(f().y)
