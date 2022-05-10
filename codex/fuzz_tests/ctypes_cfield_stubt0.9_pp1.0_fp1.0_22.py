import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class T(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int*5)]          # array of c_int

a = T()
b = ctypes.cast(a.x, ctypes.POINTER(ctypes.c_int))
b[3] = 7
print list(a.x)                              # [0, 0, 0, 7, 0]

#
# Use a pointer-field to access array members.
#

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char_p)]

s = S()
s.x = "hello"
fp = ctypes.cast(s.x, ctypes.POINTER(ctypes.c_char))
fp[2] = 'a'                                   # the string is modified
print s.x

class S1(ctypes.Structure):
    _fields_ = [('a', ctypes.c_char*5)]

class S2(ctypes.Structure):
    _fields_ = [('
