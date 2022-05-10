import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2

print s.x, s.y

ctypes.pointer(s).contents.x = 3

print s.x, s.y

s.x = 4

print s.x, s.y

s.x = 5

print s.x, s.y

s.x = 6

print s.x, s.y

s.x = 7

print s.x, s.y

s.x = 8

print s.x, s.y

s.x = 9

print s.x, s.y

s.x = 10

print s.x, s.y

s.x = 11

print s.x, s.y

s.x = 12

print s.x, s.y

s.x = 13

print s.x, s.y

s.x = 14

print s.x,
