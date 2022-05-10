import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 1
s.y = 2

print(s.x, s.y)

# ctypes.c_int is a subclass of int
print(isinstance(s.x, int))

# ctypes.c_int is a subclass of ctypes.c_long
print(isinstance(s.x, ctypes.c_long))

# ctypes.c_int is a subclass of ctypes.c_void_p
print(isinstance(s.x, ctypes.c_void_p))

# ctypes.c_int is a subclass of ctypes.c_char_p
print(isinstance(s.x, ctypes.c_char_p))

# ctypes.c_int is a subclass of ctypes.c_wchar_p
print(isinstance(s.x, ctypes.c_wchar_p))

# ctypes.c_int is a subclass of ctypes.c_char
