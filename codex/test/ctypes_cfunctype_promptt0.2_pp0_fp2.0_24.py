import ctypes
# Test ctypes.CFUNCTYPE()

import ctypes

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def add(a, b):
    return a + b

print(add(1, 2))

# Test ctypes.c_int()

import ctypes

print(ctypes.c_int(1))

# Test ctypes.c_int.value

import ctypes

a = ctypes.c_int(1)
print(a.value)

# Test ctypes.c_int.value =

import ctypes

a = ctypes.c_int(1)
a.value = 2
print(a.value)

# Test ctypes.c_int.in_dll()

import ctypes

a = ctypes.c_int(1)
a.value = 2
print(a.value)

# Test ctypes.c_int.from_address()

import ctypes

a = ctypes.c_int(1)
