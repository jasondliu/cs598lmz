import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x)
print(s.y)

print(s.__dict__)

# s.x = 3
# print(s.x)
# print(s.y)

# s.__dict__['x'] = 3
# print(s.x)
# print(s.y)

# s.__dict__['z'] = 3
# print(s.z)
# print(s.__dict__)

# s.z = 3
# print(s.z)
# print(s.__dict__)

# s.z = 3
# print(s.z)
# print(s.__dict__)

# s.__dict__['z'] = 3
# print(s.z)
# print(s.__dict__)

# s.__dict__['z'] = 3
# print(s.z)
# print(s.__dict
