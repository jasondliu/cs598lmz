import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

s = S(1)

s.x

s.x.__ctypes_from_outparam__(ctypes.c_int(2))

s.x

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int*2)]
s2 = S2(1, 2, None)

s2.x

s2.y

s2.z

s2.z.__init__(2)

s2.z

s2.z.__init__(2)

s2.z

s2.z[0]

s2.z[1]

s2.z[0] = 3

s2.z[1] = 4

s2.z

s2.z[0] = 4

s2.z

s2.z.__init__(None)

s2.z

s2.z
