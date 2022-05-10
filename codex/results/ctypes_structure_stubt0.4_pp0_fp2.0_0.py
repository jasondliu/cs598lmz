import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)
    z = ctypes.c_int(3)

s = S()
print s.x
print s.y
print s.z

print s.x.value
print s.y.value
print s.z.value

s.x.value = 10
s.y.value = 20
s.z.value = 30

print s.x.value
print s.y.value
print s.z.value

print s.x
print s.y
print s.z

print s.x.__dict__
print s.y.__dict__
print s.z.__dict__

print s.__dict__

print s.x is s.y
print s.x is s.z
print s.y is s.z

print s.x is S.x
print s.y is S.y
print s.z is S.z

print S.x is S.y
print S.x is S.z
print S
