import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

#@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
#def add(a, b):
#    return a+b

#print(add(1, 2))

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def add(a, b):
    return a+b

print(add(1, 2))

# Test ctypes.c_int(1)
#print(ctypes.c_int(1))

# Test ctypes.c_int(1).value
#print(ctypes.c_int(1).value)

# Test ctypes.c_int32
#print(ctypes.c_int32(1))

# Test ctypes.c_int32(1).value
#print(ctypes.c_int32(1).value)

# Test ctypes.c_char
#print(ctypes.c
