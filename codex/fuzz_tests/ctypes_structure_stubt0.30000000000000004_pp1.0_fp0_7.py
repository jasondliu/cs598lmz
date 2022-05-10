import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

print(type(s.x))
print(type(s.y))

print(type(s))

print(s)

print(dir(s))

print(s._fields_)

print(s.__dict__)

print(s.__doc__)

print(s.__module__)

print(s.__weakref__)

print(s.__class__)

print(s.__sizeof__())

print(s.__hash__())

print(s.__str__())

print(s.__repr__())

print(s.__format__())

print(s.__bytes__())

print(s.__lt__())

print(s.__le__())

print(s.__eq__())

print(s.__ne__())

