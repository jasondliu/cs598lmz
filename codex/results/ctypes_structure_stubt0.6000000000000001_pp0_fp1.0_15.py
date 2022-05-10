import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class S2(ctypes.Structure):
    x = ctypes.c_int

p = ctypes.pointer(S())
print(type(p))

try:
    p.contents = S2()
except TypeError as e:
    print(e)
else:
    print(p.contents)
