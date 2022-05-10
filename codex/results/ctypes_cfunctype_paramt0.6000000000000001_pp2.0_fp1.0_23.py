import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)


def mpmath_function_to_ctypes(mpmath_function):
    """
    Convert an mpmath function to a ctypes function.
    """
    def ctypes_function(x):
        return mpmath_function(x).real

    ctypes_function = FUNTYPE(ctypes_function)
    return ctypes_function


def ctypes_function_to_mpmath(ctypes_function):
    """
    Convert a ctypes function to an mpmath function.
    """
    def mpmath_function(x):
        return ctypes_function(x)

    return mpmath_function


def mpmath_function_to_python(mpmath_function):
    """
    Convert an mpmath function to a python function.
    """
    def python_function(x):
        return mpmath_function(x).real

    return python_function


def python_function_to_mpmath(python_function):
    """
    Convert a python function to an
