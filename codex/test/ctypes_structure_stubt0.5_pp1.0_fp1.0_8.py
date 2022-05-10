import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

s2 = S2()
s2.x = 1
s2.y = 2

print(s.x, s.y)
print(s2.x, s2.y)

s3 = ctypes.pointer(s)
print(s3.contents)
print(s3.contents.x, s3.contents.y)

s4 = ctypes.pointer(s2)
print(s4.contents)
print(s4.contents.x, s4.contents.y)
