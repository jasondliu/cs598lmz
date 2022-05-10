import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object, ctypes.py_object)

def c_fib(n):
    """
    Pure C implementation of Fibonacci.
    """
    if n < 2:
        return n
    else:
        return c_fib(n-2) + c_fib(n-1)

fib = FUNTYPE(c_fib)


def test_fib(n):
    """
    Compute the nth Fibonacci number using a pure Python implementation.
    """
    if n < 2:
        return n
    else:
        return test_fib(n-2) + test_fib(n-1)

def test_c_fib(n):
    """
    Compute the nth Fibonacci number using a pure C implementation.
    """
    if n < 2:
        return n
    else:
        return fib(n-2) + fib(n-1)

def test_fib_cython(n):
    """
    Compute the
