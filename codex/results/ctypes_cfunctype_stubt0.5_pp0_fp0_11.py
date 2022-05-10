import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

print(fun())

print("\n")
# ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False,
#                  use_last_error=False)
# Create a new function type. The function type may be used to create C callable function.
# The restype parameter specifies the result type. It may be None if the function returns None.
# The argtypes parameter specifies the argument types. It may be None if the function takes no arguments.
# The use_errno and use_last_error parameters are only used by Windows.
# They control whether the function should set the Windows error code for the last error.
# The use_errno parameter controls the use of the C errno variable.
# The use_last_error parameter controls the use of the GetLastError() function.
# If you are writing a Python extension module, you should never use these parameters.
# Instead, you should use the PyErr_SetFromWindowsErr() or PyErr_SetFromWindowsErrWithFilename() functions
# to set the Python exception state.
#
