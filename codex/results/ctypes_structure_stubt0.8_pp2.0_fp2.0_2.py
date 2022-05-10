import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(1)


t = S()
t.x = 1
print(t, t.x)
t.x = 2
print(t, t.x)
t.x = 3
print(t, t.x)
