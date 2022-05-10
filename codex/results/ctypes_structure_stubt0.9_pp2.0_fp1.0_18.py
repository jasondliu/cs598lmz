import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte
    y = ctypes.c_int
    z = ctypes.c_ubyte

obj = S()
print(ctypes.sizeof(obj))
print(obj.y)
print(hex(ctypes.addressof(obj.y)))
print(hex(ctypes.addressof(obj.x)))
