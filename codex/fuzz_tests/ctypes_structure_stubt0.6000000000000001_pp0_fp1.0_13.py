import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong

s = S()

print s.x
print s.y

s.x = 1
s.y = 2

print s.x
print s.y

s.x = ctypes.c_longlong(3)
s.y = ctypes.c_longlong(4)

print s.x
print s.y

s.x = ctypes.c_longlong(5)
print s.x

s.x = 6
print s.x

print s.y

s.y = ctypes.c_longlong(7)
print s.y

s.y = 8
print s.y

print s.x
print s.y

print ctypes.sizeof(s)
