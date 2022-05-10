import ctypes
ctypes.cast(0, ctypes.py_object).value

# Create a ctypes array of 10 ints
c_int_p = ctypes.POINTER(ctypes.c_int)
arr = (ctypes.c_int * 10)()

# Convert the ctypes array to a numpy array
np.ctypeslib.as_array(arr, shape=(10,))

# Convert the numpy array to a ctypes array
np.ctypeslib.as_ctypes(np.zeros(10, dtype=np.int32))

# Create a ctypes pointer to a numpy array
np.ctypeslib.as_ctypes(np.zeros(10, dtype=np.int32))._type_

# Create a numpy array from a ctypes pointer
np.ctypeslib.as_array(arr, shape=(10,))

# Convert a ctypes pointer to a python int
ctypes.cast(ctypes.pointer(ctypes.c_int(42)), ctypes.py_object).value

# Convert a python int to a ctypes pointer
ct
