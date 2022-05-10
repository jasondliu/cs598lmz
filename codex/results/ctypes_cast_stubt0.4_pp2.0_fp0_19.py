import ctypes
ctypes.cast(0, ctypes.py_object)

# Now we can store arbitrary Python objects in the array.

arr[0] = 'hello'
arr[1] = 'world'
arr[2] = '!'

for i in range(len(arr)):
    print(arr[i])

# The ctypes module also allows us to create C callable function
# pointers from Python callables.

def add(x, y):
    return x + y

import ctypes
c_add = ctypes.CFUNCTYPE(ctypes.c_int,
                         ctypes.c_int,
                         ctypes.c_int)(add)

print(c_add(1, 2))

# We can also access C libraries directly.

import ctypes
libc = ctypes.CDLL(None)
print(libc.strlen(b'hello, world'))

# Numpy is a popular library for doing numeric computations.

import numpy as np

x = np.array([1, 2, 3])
y = np.array([4
