import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"
fun()

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)

# restype 
# The result type. If None, no result is returned.

# argtypes
# A sequence of types for the arguments. Use None to indicate a flexible argument list.

# use_errno
# If True, an integer error flag is passed by reference to the C function, and a Python exception is raised on non-zero error.

# use_last_error
# If True, the Windows GetLastError() function will be called after the C function, and a Python exception will be raised on non-zero error.

# ctypes.POINTER(ctype)
# ctypes.pointer(obj)
# ctypes.byref(obj)

# ctypes.py_object

# ctypes.c_byte(val)
# ctypes.c_ubyte(val)
# ctypes.c_short(val)
# ctypes.c_ushort(val)
#
