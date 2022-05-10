import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)

x = S()
#x.x = 1
print x.x

a = ctypes.pointer(x)
print a.contents.x

x.x = 2
print a.contents.x

a.contents.x = 3
print x.x
