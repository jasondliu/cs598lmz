import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)

s = S()
print(s.x)
print(s.x.value)

s.x = 2
print(s.x)
print(s.x.value)

s.x.value = 3
print(s.x)
print(s.x.value)

s.x = ctypes.c_int(4)
print(s.x)
print(s.x.value)

s.x.value = 5
print(s.x)
print(s.x.value)

s.x = 6
print(s.x)
print(s.x.value)

s.x = ctypes.c_int(7)
print(s.x)
print(s.x.value)

s.x.value = 8
print(s.x)
print(s.x.value)

s.x = 9
print(s.x)
print(s.x.value)

s.x = ctypes.c_int(10)
print(
