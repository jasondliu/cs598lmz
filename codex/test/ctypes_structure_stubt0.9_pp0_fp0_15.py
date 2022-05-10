import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ulong()
    tag = ctypes.c_ushort()
    
s = S();

s.x =  0x12345678
s.tag = 10

libc = ctypes.CDLL(None)

stringbuf = "<+" + "I" * 100 + "pHI"
