import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32(1)

p = ctypes.pointer(S())
print(p.contents.x)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
