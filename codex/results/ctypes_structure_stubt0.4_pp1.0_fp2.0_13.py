import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

    def __str__(self):
        return "<S x=%s>" % self.x

s = S()
s.x = 42

print(s)

s = ctypes.cast(ctypes.pointer(s), ctypes.POINTER(S))
print(s.contents)

s = ctypes.cast(ctypes.pointer(s.contents), ctypes.POINTER(S))
print(s.contents)

s = ctypes.cast(ctypes.pointer(s.contents), ctypes.POINTER(S))
print(s.contents)

s = ctypes.cast(ctypes.pointer(s.contents), ctypes.POINTER(S))
print(s.contents)

s = ctypes.cast(ctypes.pointer(s.contents), ctypes.POINTER(S))
print(s.contents)

s = ctypes.cast(ctypes.pointer(s.contents), ctypes.POINTER(S))
print(s.contents)

