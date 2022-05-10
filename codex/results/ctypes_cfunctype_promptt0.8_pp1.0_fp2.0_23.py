import ctypes
# Test ctypes.CFUNCTYPE
def run_cfunctype_test():
    # calling an int-returning function
    c_int_to_int = ctypes.CFUNCTYPE(ctypes.c_int)(lambda: 3)
    # calling a float-returning function
    c_float_to_float = ctypes.CFUNCTYPE(ctypes.c_float)(lambda: 3.0)
    if c_int_to_int() != 3:
        return -1
    if c_float_to_float() != 3.0:
        return -1

    # float-returning function accepting float
    c_float_to_float = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_float)(
        lambda x: x + 1.0)
    if c_float_to_float(1.0) != 2.0:
        return -1

    # int-returning function accepting int, float, int
    c_int_to_float = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.
