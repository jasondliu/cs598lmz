import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_py_object_return():
    assert fun() == "hello"

def test_py_object_return_with_error():
    try:
        ctypes.pythonapi.PyErr_SetString(ctypes.py_object(ValueError), b"hello")
        assert 0
    except ValueError:
        pass

def test_py_object_return_with_error2():
    try:
        ctypes.pythonapi.PyErr_SetString(ctypes.py_object(ValueError), b"hello")
        ctypes.pythonapi.PyErr_SetString(ctypes.py_object(ValueError), b"hello")
        assert 0
    except ValueError:
        pass

def test_py_object_return_with_error3():
    try:
        ctypes.pythonapi.PyErr_SetString(ctypes.py_object(ValueError), b"hello")
        ctypes.pythonapi.PyErr_SetString(ctypes.py_object(ValueError), b"hello")
