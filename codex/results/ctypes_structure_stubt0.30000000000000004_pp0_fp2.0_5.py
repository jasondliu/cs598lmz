import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s = S()
s.x = 1
s.y = 2
print(s.x, s.y)

print(s.__dict__)
print(s._fields_)
print(s._asdict())

print(s.__sizeof__())
print(s.__reduce__())
print(s.__reduce_ex__(2))
print(s.__reduce_ex__(2)[0](*s.__reduce_ex__(2)[1]))

print(s.__reduce_ex__(2)[0](*s.__reduce_ex__(2)[1]).__dict__)
print(s.__reduce_ex__(2)[0](*s.__reduce_ex__(2)[1])._fields_)
print(s.__reduce_ex__(2)[0](*s.__reduce
