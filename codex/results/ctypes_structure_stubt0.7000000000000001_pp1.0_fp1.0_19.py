import ctypes

class S(ctypes.Structure):
    x = (ctypes.c_uint * 4)()
    y = ctypes.c_uint()
    z = ctypes.c_uint()

s = S()

s.x[0] = 0x11223344
s.x[1] = 0x55667788
s.x[2] = 0x99aabbcc
s.x[3] = 0xddeeff00

print s.x
print s.y
print s.z
