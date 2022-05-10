import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)
    _fields_ = [("x", ctypes.c_int)]

s = S()
print s.x

s.x = 1
print s.x

print ctypes.cast(ctypes.pointer(s), ctypes.POINTER(ctypes.c_int))[0]

class S2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

s2 = S2(1)
print s2.x

class S3(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class S4(S3):
    _fields_ = [("y", ctypes.c_int)]

s4 = S4(1)
print s4.x
print s4.y

class S5(S3):
    _fields_ = [("y", ctypes.c_int)]

print ctypes._subarray(ctypes.c_int, S5, "y")

class S6
