import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x, s.y, s.z)

# ctypes.c_int.from_address(id(s))

print(ctypes.cast(id(s), ctypes.POINTER(ctypes.c_int)))

# print(ctypes.cast(id(s), ctypes.POINTER(ctypes.c_int)).contents)

print(ctypes.cast(id(s), ctypes.POINTER(ctypes.c_int)).contents.value)

print(ctypes.cast(id(s), ctypes.POINTER(ctypes.c_int)).contents.value)

# print(ctypes.cast(id(s), ctypes.POINTER(ctypes.c_int)).contents.value)

