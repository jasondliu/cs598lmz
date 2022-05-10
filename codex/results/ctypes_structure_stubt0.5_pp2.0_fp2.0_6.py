import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(1)
    y = ctypes.c_long(2)


s = S()
print s.x, s.y
print type(s.x), type(s.y)
print ctypes.sizeof(s.x), ctypes.sizeof(s.y)
print ctypes.sizeof(s)

print ctypes.cast(ctypes.pointer(s), ctypes.POINTER(ctypes.c_long))[0]
print ctypes.cast(ctypes.pointer(s), ctypes.POINTER(ctypes.c_long))[1]

print ctypes.cast(ctypes.pointer(s), ctypes.POINTER(ctypes.c_long))[2]
print ctypes.cast(ctypes.pointer(s), ctypes.POINTER(ctypes.c_long))[3]
