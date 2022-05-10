import ctypes
ctypes.cast(a, ctypes.c_void_p).value

# To convert back to a numpy array, you can use
# ctypes.cast(<c_void_p>, ctypes.POINTER(ctypes.c_byte))
# to get a pointer to the first element of the array,
# then use numpy's ndarray.__new__ to create an array
# from the pointer, setting the dtype and shape
# appropriately.

# Or you can use numpy.ctypeslib.as_array, which does
# all of this for you.

# The following is a complete example of how to convert
# a numpy array to and from a ctypes array.

import numpy
import ctypes

# Create a numpy array.
a = numpy.arange(12, dtype=numpy.float32)
# Reshape it to 3x4.
a.shape = (3, 4)
print(a)

# Cast the numpy array to a ctypes array.
ctypes_array = ctypes.cast(a.ctypes.data, ctypes
