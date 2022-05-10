import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

print(s.__sizeof__())
print(s.__dict__)
print(s.__dir__())
print(s.__doc__)
print(s.__format__('%s'))
print(s.__getattribute__('x'))
print(s.__hash__())
print(s.__init__())
print(s.__module__)
print(s.__new__(S))
print(s.__reduce__())
print(s.__reduce_ex__(2))
print(s.__repr__())
print(s.__setattr__('x', 3))
print(s.__sizeof__())
print(s.__str__())
print(s.__subclasshook__())
print(s.__weakref__)
