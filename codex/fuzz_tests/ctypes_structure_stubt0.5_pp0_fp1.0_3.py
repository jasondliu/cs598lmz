import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

s = S()
s.x = 1
s.y = 2
print s.x, s.y

print ctypes.sizeof(S)

class T(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

t = T()
t.x = 1
t.y = 2
print t.x, t.y

print ctypes.sizeof(T)
