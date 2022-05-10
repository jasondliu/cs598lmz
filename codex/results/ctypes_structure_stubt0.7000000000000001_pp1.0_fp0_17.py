import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long(1)
    y = ctypes.c_long(2)
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]


s = S()
print s.x
print s.y

s.x = 2
s.y = 3

print s.x
print s.y

ctypes.c_long.from_address(ctypes.addressof(s)).value = 10
print s.x
print s.y

print ctypes.addressof(s)
print ctypes.addressof(s.x)
print ctypes.addressof(s.y)
