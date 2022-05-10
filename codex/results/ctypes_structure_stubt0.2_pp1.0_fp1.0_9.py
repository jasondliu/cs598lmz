import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

print(s.__dict__)
print(s.__class__)
print(s.__class__.__dict__)

print(S.__dict__)
print(S.__class__)
print(S.__class__.__dict__)

print(ctypes.Structure.__dict__)
print(ctypes.Structure.__class__)
print(ctypes.Structure.__class__.__dict__)

print(ctypes.__dict__)
print(ctypes.__class__)
print(ctypes.__class__.__dict__)

print(object.__dict__)
print(object.__class__)
print(object.__class__.__dict__)

print(type.__dict__)
print(type.__class__)
print(type.__class__.__dict__
