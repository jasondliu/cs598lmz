import ctypes
# Test ctypes.CFUNCTYPE

################################################################
#
#  Declare the return type and argument types of the C callback
#  function
#
################################################################

# int32_t (*)(real64_t, real64_t)
callback_type = ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_double, ctypes.c_double)

################################################################
#
#  Declare the C function prototype
#
################################################################

# int32_t
# c_function(int32_t (*callback)(real64_t, real64_t),
#            real64_t arg1,
#            real64_t arg2)

c_function = ctypes.CDLL('libfoo.so').c_function
c_function.argtypes = [callback_type, ctypes.c_double, ctypes.c_double]
c_function.restype = ctypes.c_int32

################################################################
#
#  Define Python callback function
#
################################################################

def python_callback(arg1, arg2):
    return int(arg
