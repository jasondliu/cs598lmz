import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S()
print(s.x)
s.x = 5
print(s.x)

print(s.__dict__)
print(s._fields_)
print(s._fields_[0])
print(s._fields_[0][0])
print(s._fields_[0][1])
print(s._fields_[0][2])

s.x = 6
print(s.x)
print(s._fields_[0][0])
print(s._fields_[0][1])
print(s._fields_[0][2])

print(s._fields_[0][1](s))

print(s._fields_[0][1](s, 7))

print(s.x)
print(s._fields_[0][0])
print(s._fields_[0][1])
print(s._fields_[0][2])

print(s._fields_[0][0])
print(s._fields_[0][1])
print(s._fields_[
