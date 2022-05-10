import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char

s = S()
s.x = 'a'
assert s.x == 'a'
assert s.x != 'b'

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_char)]

s = S()
s.x = 'a'
assert s.x == 'a'
assert s.x != 'b'

class S(ctypes.Structure):
    x = ctypes.c_char * 2

s = S()
s.x = 'ab'
assert s.x == 'ab'
assert s.x != 'ac'

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_char * 2)]

s = S()
s.x = 'ab'
assert s.x == 'ab'
assert s.x != 'ac'

class S(ctypes.Structure):
    x = ctypes.c_longlong

s = S()
s.x = -922337203685
