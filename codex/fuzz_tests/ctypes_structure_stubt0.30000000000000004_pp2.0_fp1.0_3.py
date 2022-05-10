import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
print s.x
print s.y
print s.z

s.x = 1
s.y = 2
s.z = 3

print s.x
print s.y
print s.z

s.x = 4
s.y = 5
s.z = 6

print s.x
print s.y
print s.z

s.x = 7
s.y = 8
s.z = 9

print s.x
print s.y
print s.z

s.x = 10
s.y = 11
s.z = 12

print s.x
print s.y
print s.z

s.x = 13
s.y = 14
s.z = 15

print s.x
print s.y
print s.z

s.x = 16
s.y = 17
s.z = 18

print s.x
print s.y
print s
