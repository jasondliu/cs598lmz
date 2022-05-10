import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_cfunc():
    assert fun() == "hello"

def test_cfunc_error():
    try:
        fun()
    except TypeError:
        pass
    else:
        assert False, "did not raise"

def test_cfunc_error_2():
    try:
        fun()
    except TypeError:
        pass
    else:
        assert False, "did not raise"

def test_cfunc_error_3():
    try:
        fun()
    except TypeError:
        pass
    else:
        assert False, "did not raise"
