import ctypes

class S(ctypes.Structure):
    x = 10
    _fields_ = [
            ('y', ctypes.c_long),
            ('z', ctypes.c_char_p)
    ]
s = S()
s.x = 1
s.y = 2
s.z = b'abc'

s.x = 1
s.y = 2
s.z = b'abc'

s.x = 1
s.y = 2
s.z = b'abc'

s.x = 1
s.y = 2
s.z = b'abc'

s.x = 1
s.y = 2
s.z = b'abc'

s.x = 1
s.y = 2
s.z = b'abc'

s.x = 1
s.y = 2
s.z = b'abc'

s.x = 1
s.y = 2
s.z = b'abc'

s.x = 1
s.y = 2
s.z = b'abc'

s.x = 1
s.y = 2
