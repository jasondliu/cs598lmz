import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint64


s = S()
s.x = 0xFFFFFFFFFFFFFFFF

print "%x" % s.x
