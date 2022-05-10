import ctypes
# Test ctypes.CField

class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class X(S):
    _fields_ = [("c", S)]

print X.c.a
print X.c.b

x = X()
print x.c.a
print x.c.b

# Test ctypes.CField.from_param

class Int(ctypes.c_int):
    @classmethod
    def from_param(cls, obj):
        return obj+1

class S(ctypes.Structure):
    _fields_ = [("a", Int)]

print S.a
print S.a.from_param(1)

s = S()
print s.a


# Test ctypes.CField.from_address

class S(ctypes.Structure):
    _fields_ = [("a", Int), ("b", Int)]

s = S()
print s.a
print s.b

s.a
