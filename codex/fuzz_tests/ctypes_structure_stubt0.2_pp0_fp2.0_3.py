import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print s.x
print s.y
print s.z

print s.__dict__

print s.__dict__["x"]
print s.__dict__["y"]
print s.__dict__["z"]

print s.__dict__["x"] = 4
print s.__dict__["y"] = 5
print s.__dict__["z"] = 6

print s.x
print s.y
print s.z

print s.__dict__

print s.__dict__["x"]
print s.__dict__["y"]
print s.__dict__["z"]

print s.__dict__["x"] = 7
print s.__dict__["y"] = 8
print s.__dict__["z"] = 9

print s.x
print s.y
print s.z

print s.
