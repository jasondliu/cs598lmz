import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = 1
s.y = 2
print(s.x, s.y)

# ctypes.c_int.from_buffer(s, 0)
# ctypes.c_int.from_buffer(s, 4)

print(s.contents)
print(s.contents.x)

print(ctypes.cast(s, ctypes.c_int_p).contents)
print(ctypes.cast(s, ctypes.c_int_p).contents.value)

print(ctypes.cast(s, ctypes.c_int_p).value)

print(ctypes.cast(s, ctypes.c_int_p)[0])
print(ctypes.cast(s, ctypes.c_int_p)[1])

print(ctypes.cast(s, ctypes.c_int_p)[0] == s.contents)
print(ctypes.cast(s, ctypes.c
