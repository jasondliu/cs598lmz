import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()
    z = ctypes.c_int()

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x, s.y, s.z)

s2 = S()
s2.x = 4
s2.y = 5
s2.z = 6

print(s2.x, s2.y, s2.z)

s2 = s

print(s2.x, s2.y, s2.z)

s.x = 10
s.y = 20
s.z = 30

print(s.x, s.y, s.z)
print(s2.x, s2.y, s2.z)

s2.x = 40
s2.y = 50
s2.z = 60

print(s.x, s.y, s.z)
print(s2.x, s2.y, s2.z)

s = S
