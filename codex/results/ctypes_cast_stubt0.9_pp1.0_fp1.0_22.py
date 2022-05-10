import ctypes
ctypes.cast(base_pointer, ctypes.POINTER(ctypes.c_void_p)).contents.value

# Casting pointers to ctypes arrays
b = np.arange(1, 10)
base_pointer, read_only_flag = b.__array_interface__['data']
if not read_only_flag:
    arr_ctypes = ctypes.cast(base_pointer, ctypes.POINTER(ctypes.c_int * len(b)))
    b_pointer = arr_ctypes.contents

# Get a pointer to `b`
b_pointer.contents  # 1

# Change the value at `b_pointer`
b_pointer.contents = 200
b_pointer.contents  # 200
b # array([200, 2, 3, 4, 5, 6, 7, 8, 9])

b_pointer[3] = 5
b  # array([200, 2, 3, 5, 5, 6, 7, 8, 9])

# I have a pointer to a function. How can I call it?
import numpy as np
a = np
