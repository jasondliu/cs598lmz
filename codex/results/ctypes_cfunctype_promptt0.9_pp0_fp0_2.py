import ctypes
# Test ctypes.CFUNCTYPE


def type_test():

    ctypes.CFUNCTYPE(ctypes.c_int)


# Test ctypes.PyCFuncPtr and ctypes.CFUNCTYPE.from_function
def function_test():

    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int,
                     use_errno=True)
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int,
                     use_last_error=True)
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int,
                     use_last_error=True, use_errno=True)
    ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int,
                     use_
