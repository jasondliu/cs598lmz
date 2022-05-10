import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)

foo = S()
print(foo.x, foo.y)
foo.z = ctypes.c_int(3)
print(foo.x, foo.y, foo.z)
