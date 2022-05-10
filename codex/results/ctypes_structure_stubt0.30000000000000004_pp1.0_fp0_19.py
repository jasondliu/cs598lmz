import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)
print(s.__dict__)
print(s._fields_)
print(s._asdict())

print(s._fields_[0][0], s._fields_[0][1])
print(s._fields_[1][0], s._fields_[1][1])

print(s._asdict()['x'], s._asdict()['y'])

print(s._fields_[0][0] in s._asdict())
print(s._fields_[1][0] in s._asdict())

print(s._fields_[0][0] in s.__dict__)
print(s._fields_[1][0] in s.__dict__)

print(s._fields_[0][0] in dir(s))
print(s._fields_[1][0] in dir(s))

print(s._fields_
