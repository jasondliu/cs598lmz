import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ulong()
    tag = ctypes.c_ushort()
    
s = S();

s.x =  0x12345678
s.tag = 10

libc = ctypes.CDLL(None)

stringbuf = "<+" + "I" * 100 + "pHI"
stringbuf = bytes(stringbuf, "ascii") + (ctypes.c_ubyte * (ctypes.sizeof(ctypes.c_ubyte) * 100)).from_buffer(s.x)

#libc.printf(stringbuf, s.tag, 1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56
