import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()

    def __init__(self, **kwds):
        self.x.value = kwds.get('x', 0)
        self.x.value += 42
        print(self.x)

s = S(x=42)
print(s.x)
print(s.x.value)
print()
s.x = 36
s.x *= 2
print(s.x)
print(s.x.value)
print()
s.x = ctypes.c_long(36)
s.x *= 2
print(s.x)
print(s.x.value)
print()
s.x = ctypes.c_long(36)
s._x_ = s.x * 2
print(s.x)
print(s.x.value)
print()
s.x.value += 1
print(s.x)
print(s.x.value)
print()
# del s.x
print(s.x)
print(s.x.value)
print()
