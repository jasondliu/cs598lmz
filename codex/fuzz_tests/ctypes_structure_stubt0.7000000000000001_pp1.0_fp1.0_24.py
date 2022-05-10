import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(5)
    y = ctypes.c_int(6)
    _fields_ = [("x", ctypes.c_uint), ("y", ctypes.c_uint)]


class S2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_uint)]

s = S()
l = ctypes.c_long.from_address(ctypes.addressof(s))
print l.value
print l.value & 0xffffffff

s2 = S2()
l2 = ctypes.c_long.from_address(ctypes.addressof(s2))
print l2.value
print l2.value & 0xffffffff

print ctypes.addressof(s2)
print ctypes.addressof(s)
