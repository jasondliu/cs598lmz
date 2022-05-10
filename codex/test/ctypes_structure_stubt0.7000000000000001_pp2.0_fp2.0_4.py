import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(1)
    y = ctypes.c_long(2)

s = S()

for attr in dir(s):
    if not attr.startswith('__'):
        print(attr, getattr(s, attr))
