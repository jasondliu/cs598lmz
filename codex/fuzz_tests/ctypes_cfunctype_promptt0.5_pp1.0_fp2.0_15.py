import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def add(a, b):
    return a + b

print(add(1, 2))

# Test ctypes.CFUNCTYPE(None, ctypes.c_char_p)
@ctypes.CFUNCTYPE(None, ctypes.c_char_p)
def print_string(string):
    print(string.decode())

print_string(b"Hello world!")

# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
def add3(a, b, c):
    return a + b + c


