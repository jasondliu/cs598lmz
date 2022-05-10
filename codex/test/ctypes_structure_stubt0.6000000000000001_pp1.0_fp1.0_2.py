import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32
    y = ctypes.c_int32
    z = ctypes.c_int32
    _fields_ = [('x', ctypes.c_int32),
                ('y', ctypes.c_int32),
                ('z', ctypes.c_int32)]

s = S(1,2,3)
s.x = 2
s.y = 3
s.z = 4
print(s.x, s.y, s.z)

s = S()
S.x.__set__(s, 4)
S.y.__set__(s, 5)
S.z.__set__(s, 6)
print(s.x, s.y, s.z)
