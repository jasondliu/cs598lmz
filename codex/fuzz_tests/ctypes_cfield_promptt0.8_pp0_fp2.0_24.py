import ctypes
# Test ctypes.CField is hashable.
hash(ctypes.CField())

class Structure(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]
    def __eq__(self, other):
        if not isinstance(other, Structure):
            return NotImplemented
        return self.a == other.a and self.b == other.b

s1 = Structure()
s1.a = 1
s1.b = 2

s2 = Structure()
s2.a = 1
s2.b = 2

s3 = Structure()
s3.a = 1
s3.b = 3

hash(s1)
hash(s2)
hash(s3)

s1 == s2
s1 == s3
s2 == s3

# Test ctypes.CData is hashable.
hash(ctypes.c_int())
hash(ctypes.c_void_p())
hash(ctypes.c_wchar())
# Test ctypes.CData is not hash
