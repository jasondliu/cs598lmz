import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)
print(s.__dict__)
print(s._fields_)

#print(s.x + s.y)

print(ctypes.sizeof(s))
print(ctypes.byref(s))
print(ctypes.addressof(s))
print(ctypes.addressof(s.x))
print(ctypes.addressof(s.y))

print(ctypes.cast(ctypes.addressof(s.x), ctypes.POINTER(ctypes.c_int)))
