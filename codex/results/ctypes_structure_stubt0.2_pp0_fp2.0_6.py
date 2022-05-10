import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S()
s.x = 1

print(s.x)
print(s.x.value)
print(s.x.__dict__)
print(s.x.__class__)
print(s.x.__class__.__bases__)
print(s.x.__class__.__bases__[0].__bases__)
print(s.x.__class__.__bases__[0].__bases__[0].__bases__)
print(s.x.__class__.__bases__[0].__bases__[0].__bases__[0].__bases__)
print(s.x.__class__.__bases__[0].__bases__[0].__bases__[0].__bases__[0].__bases__)
print(s.x.__class__.__bases__[0].__bases__[0].__bases__[0].__bases__[0].__bases__[0].__b
