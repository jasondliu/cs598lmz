import ctypes
# Test ctypes.CFUNCTYPE and ctypes.PYFUNCTYPE
if 1:
    # call a simple C function
    cdll.load("libc.dylib")

    prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    paramflags = (1,)
    p = prototype(("test_func", dll), paramflags)
    res = p(10)
    assert res == 42, res

    # call a simple Python function
    pyfunc = lambda x: x
    prototype = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
    pythonsimple = prototype(pyfunc)
    res = pythonsimple(42)
    assert res == 42, res

    # call a Python function which raises an exception
    pyfunc = lambda x: 0 / x
    prototype = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
    pythonsimple = prototype(pyfunc)
    raises(ZeroDivisionError, pythonsimple
