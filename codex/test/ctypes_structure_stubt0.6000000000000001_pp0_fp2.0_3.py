import ctypes

class S(ctypes.Structure):
    x = ctypes.c_bool()

t = S()
t.x = True
print(t.x)

t.x = False
print(t.x)
