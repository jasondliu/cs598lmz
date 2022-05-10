import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_float

s = S()
s.x = 3
s.y = 4.5

print s.x, s.y

print ctypes.sizeof(s)

print ctypes.addressof(s.x)
print ctypes.addressof(s.y)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_float)]

s2 = S2()
s2.x = 3
s2.y = 4.5

print s2.x, s2.y

print ctypes.sizeof(s2)

print ctypes.addressof(s2.x)
print ctypes.addressof(s2.y)

s3 = ctypes.cast(s2, ctypes.POINTER(S))
print s3.contents.x, s3.contents.y

s4 = ctypes.cast(s3, ctypes.PO
