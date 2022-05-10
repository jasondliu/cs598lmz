import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)
    z = ctypes.c_int(3)

s = S()
print s.x
print s.y
print s.z

print s.__dict__
print s.__dict__.keys()
print s.__dict__.values()

print s._fields_
print s._fields_[0]
print s._fields_[1]
print s._fields_[2]

for i in range(len(s._fields_)):
    print s._fields_[i][0], getattr(s, s._fields_[i][0])

for i in range(len(s._fields_)):
    print s._fields_[i][0], getattr(s, s._fields_[i][0])

s.x = 5
s.y = 6
s.z = 7

for i in range(len(s._fields_)):
    print s._fields_[i][0], getattr(s, s._fields_
