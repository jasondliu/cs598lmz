import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong

def f():
    return S(1, 2)

s = f()
print(s.x)
print(s.y)

s = S(1, 2)
print(s.x)
print(s.y)
