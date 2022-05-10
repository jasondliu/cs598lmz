import ctypes
ctypes.cast(ctypes.pointer(c), ctypes.POINTER(ctypes.c_double))

# Create the array in ctypes
array_1d_double = ctypes.c_double * 3
print array_1d_double

# Fill the arrays with data
array_1d_double[0] = 0.0
array_1d_double[1] = 1.0
array_1d_double[2] = 2.0

###############################################################################
# Now let's convert the ctypes array to a numpy array

a = np.ctypeslib.as_array(array_1d_double)
print a

# Convert a numpy array to a ctypes array

b = np.arange(12, dtype=np.float32).reshape(3,4)
# Create a ctypes array allocated using ctypes malloc
# NOTE: I'm using 'double' here because I'm lazy, but this is actually
# 'float' in the C code.
array_2d_double = ctypes.c_double * (4 * 3)
# Call as
