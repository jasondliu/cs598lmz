import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
print s.x, s.y
s.x = 1
s.y = 2
print s.x, s.y

print ctypes.sizeof(s)
print ctypes.sizeof(ctypes.c_int)
print ctypes.sizeof(ctypes.c_int())

print ctypes.addressof(s.x), ctypes.addressof(s.y)
print ctypes.addressof(s)

s2 = S.from_address(ctypes.addressof(s))
print s2.x, s2.y
s2.x += 1
print s.x, s.y

print ctypes.memset(ctypes.addressof(s), 0, ctypes.sizeof(s))
print s.x, s.y

print ctypes.string_at(ctypes.addressof(s), ctypes.sizeof(s))

print ctypes.memmove(ctypes.add
