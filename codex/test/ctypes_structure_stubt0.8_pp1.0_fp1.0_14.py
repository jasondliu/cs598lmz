import ctypes

class S(ctypes.Structure):
    x = 1

p = ctypes.POINTER(S)()
p.x = 2
print(p.x)   # print 2 and not 1.
