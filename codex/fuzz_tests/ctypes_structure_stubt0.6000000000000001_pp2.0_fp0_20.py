import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 100
s.y = 200

print s.x, s.y

#print ctypes.addressof(s)

print ctypes.addressof(s.x)
print ctypes.addressof(s.y)

print ctypes.sizeof(s)
print ctypes.sizeof(s.x)
print ctypes.sizeof(s.y)

#print ctypes.byref(s)

#print ctypes.byref(s.x)
#print ctypes.byref(s.y)

print ctypes.string_at(ctypes.addressof(s), ctypes.sizeof(s))

print ctypes.string_at(ctypes.addressof(s.x), ctypes.sizeof(s.x))
print ctypes.string_at(ctypes.addressof(s.y), ctypes.sizeof(s.y))

print ctypes.string_at
