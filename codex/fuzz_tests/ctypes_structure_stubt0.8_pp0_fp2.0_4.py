import ctypes

class S(ctypes.Structure):
    x = ctypes.c_byte
    y = ctypes.c_byte
    z = ctypes.c_short
    _pack_ = 1

def f():
    return S(x=1, y=2, z=3)

@tiramisu.jit
def g(a):
    a.x = 10
    a.y = 11
    a.z = 12

a = f()
print(a.x, a.y, a.z)
g(a)
print(a.x, a.y, a.z)
