import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 10
s.y = 20

print(s.x, s.y)

# ctypes.c_int.from_address(id(s)).value = 100

print(s.x, s.y)
