import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)

with open(__file__, "rb") as f:
    data = f.read()
print(data)

