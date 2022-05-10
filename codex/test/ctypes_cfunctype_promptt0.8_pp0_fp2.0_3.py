import ctypes
# Test ctypes.CFUNCTYPE.

# This is the type of each element of the array, so an array of 20 elements
# of this type can store the 20 function arguments.  On most machines,
# sizeof(short) == 2.
class short_array(ctypes.Array):
    _length_ = 20
    _type_ = ctypes.c_short

# This is the type of the actual array.
short_array_20 = short_array * 20

# And this is the callback function type.
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int,
                                ctypes.POINTER(short_array_20))

