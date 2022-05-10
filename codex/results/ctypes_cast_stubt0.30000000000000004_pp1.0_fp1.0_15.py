import ctypes
ctypes.cast(ctypes.pointer(c_int(0)), ctypes.POINTER(ctypes.c_int))

# Convert ctypes arguments to lists
ctypes.cast( (c_int * 3)(1, 2, 3), POINTER(c_int) )

# Create ctypes arrays
array_1d_int = c_int * 5
array_1d_int(*range(5))

array_2d_int = c_int * 3 * 2
array_2d_int(*range(6))

# Cast ctypes arrays to pointers
pointer(array_1d_int(*range(5)))

pointer(array_2d_int(*range(6)))

# Create and cast ctypes arrays in one step
pointer((c_int * 5)(*range(5)))

pointer((c_int * 3 * 2)(*range(6)))

# Accessing ctypes arrays
a = array_1d_int(*range(5))
print(a[0], a[1])

a = array_2d_int(*range(6))
print(a[0
