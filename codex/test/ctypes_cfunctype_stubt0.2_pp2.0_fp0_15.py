import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_ctypes_py_object():
    assert fun() is None

def test_ctypes_py_object_exception():
    try:
        raise ValueError
    except ValueError:
        e = sys.exc_info()[1]
        assert fun(e) is e

def test_ctypes_py_object_exception_with_tb():
    try:
        raise ValueError
    except ValueError:
        e = sys.exc_info()
        assert fun(*e) is e[1]

def test_ctypes_py_object_exception_with_tb_and_extra_arg():
    try:
        raise ValueError
    except ValueError:
        e = sys.exc_info()
        assert fun(*e, 42) is e[1]

def test_ctypes_py_object_exception_with_tb_and_kwargs():
    try:
        raise ValueError
    except ValueError:
        e = sys.exc_info()
