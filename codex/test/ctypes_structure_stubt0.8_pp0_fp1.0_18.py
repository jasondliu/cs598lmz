import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(1.0)

with open("c.dat", "w") as fout:
    s = S()
