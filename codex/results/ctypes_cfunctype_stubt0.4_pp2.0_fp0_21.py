import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

@FUNTYPE
def fun(x):
    return x

@FUNTYPE
def fun(x, y):
    return x+y

@FUNTYPE
def fun(x, y, z):
    return x+y+z

fun()
fun(1)
fun(1,2)
fun(1,2,3)

# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
#   restype - The result type.
#   argtypes - The argument types.
#   use_errno - If True, the function will check for the C function setting errno,
#               and will raise an OSError exception if the C function returns -1.
#               The exception object will have an errno attribute containing the
#               value of the C errno variable.
#   use_last_error - If True, the function will check for the C function setting
#                    the Win32 last error code, and will raise a WindowsError
#                    exception if the C function returns -1
