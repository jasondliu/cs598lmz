import ctypes

class S(ctypes.Structure):
    x = 16

    _fields_ = [("y", ctypes.c_void_p),
                ("z", ctypes.c_void_p)]


s = S()
print(hex(ctypes.addressof(s)))
print(hex(ctypes.addressof(s.y)))
print(hex(ctypes.addressof(s.z)))
