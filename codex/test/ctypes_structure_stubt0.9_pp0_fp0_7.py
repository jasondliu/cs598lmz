import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32()
    y = ctypes.c_uint16()
    z = ctypes.c_uint8()
    w = ctypes.c_byte()

ob = S()

print(ob.x, ob.y, ob.z, ob.w)
