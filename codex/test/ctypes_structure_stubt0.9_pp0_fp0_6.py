import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(1)

i = 0
while True:
    i += 1
