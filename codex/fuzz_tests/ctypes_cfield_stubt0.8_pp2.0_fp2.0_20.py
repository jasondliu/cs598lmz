import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

S.x.offset
S.x.offset == ctypes.c_int.offset

class T(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

T.x.offset
T.y.offset

ctypes.sizeof(ctypes.c_int) == T.y.offset - T.x.offset

class R(ctypes.Structure):
    _pack_ = 4
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int),
                ('w', ctypes.c_int),
                ('a', ctypes.c_int),
                ('b', ctypes.c_int),
                ('c', ctypes.c_int),
                ('d', ctypes.c_int)]

ctypes.sizeof(R)

(16, 32, 64)[sys.maxsize > 2**32]

R.z.
