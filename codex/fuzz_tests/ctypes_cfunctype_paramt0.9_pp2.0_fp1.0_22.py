import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def test_error(code, py_func, c_func):
    try:
        result = py_func(code)
    except:
        pass
    else:
        raise FailTest('{0} should have raised TypeError'.format(py_func.__name__))
    result = c_func(code)
    assert result == -1, '{0} did not return expected value'.format(py_func.__name__)

def test_no_error(code, py_func, c_func):
    result = py_func(code)
    assert result == c_func(code)

FUNC_PYTHON_OPEN = pythonapi.fopen
FUNC_C_OPEN = ctypes.CDLL(None).fopen
FUNC_PYTHON_OPEN.restype = ctypes.c_void_p
FUNC_PYTHON_OPEN.argtypes = (ctypes.c_char_p, ctypes.c_char_p)
FUN
