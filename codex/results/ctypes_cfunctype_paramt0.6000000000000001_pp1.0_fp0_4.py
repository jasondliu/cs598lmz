import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int, ctypes.c_double)

#
# Define the call-back functions
#
@FUNTYPE
def py_func(n, x):
    return n * x

@FUNTYPE
def py_func_err(n, x):
    raise RuntimeError("Error in call-back function")

def test_py_func(func):
    """Test a Python call-back function."""

    #
    # Initialize the library.
    #
    lib.test_init(1, 1)

    #
    # Set the Python call-back function.
    #
    cb_func = FUNTYPE(func)
    lib.test_set_py_func(cb_func)

    #
    # Call the wrapped function and check the result.
    #
    res = lib.test_call_py_func()
    if res != 4.0:
        raise RuntimeError("Unexpected result")

    #
    # Finalize the library.
    #
    lib.test_finalize()


