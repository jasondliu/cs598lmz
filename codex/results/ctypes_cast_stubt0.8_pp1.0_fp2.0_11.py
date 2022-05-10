import ctypes
ctypes.cast(a.data, ctypes.py_object).value

# 4) In the previous lesson you saw that numpy has a bitwise_xor function.
# In this exercise you will create your own function that applies the
# bitwise_xor operation to two arrays using the ctypes library.
# Your function should work for two boolean NumPy arrays of the same size.

import ctypes

# Create ctypes arrays:
dtype = ctypes.c_uint8

a_ctypes = (ctypes.c_uint8 * len(a)).from_buffer(a)
b_ctypes = (ctypes.c_uint8 * len(b)).from_buffer(b)

uint8_t = ctypes.c_uint8
uint8_t_p = ctypes.POINTER(uint8_t)

# Create ctypes pointer to ctypes array
a_ctypes_p = ctypes.cast(a_ctypes, uint8_t_p)
b_ctypes_p = ctypes.cast(b_ctypes, uint8_t_p)

#
