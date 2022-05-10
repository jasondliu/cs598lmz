import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int),
    ]

print(S.x)
print(S.y)
print(S._fields_)

# ctypes.c_int(42)
# ctypes.c_int(42).value
# ctypes.c_int(42).value == 42

# ctypes.c_int(42).value = 43
# ctypes.c_int(42).value

# ctypes.c_int(42).value += 1
# ctypes.c_int(42).value

# ctypes.c_int(42).value = 'hello'

# ctypes.c_int(42).value = 3.14

# ctypes.c_int(42).value = [1, 2, 3]

# ctypes.c_int(42).value = (1, 2, 3)

# ctypes.c_int(42).value =
