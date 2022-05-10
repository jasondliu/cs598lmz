import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42

def test_fun_with_arg():
    try:
        fun(1)
    except TypeError:
        pass
    else:
        raise AssertionError("did not raise")

def test_fun_with_kwargs():
    try:
        fun(x=1)
    except TypeError:
        pass
    else:
        raise AssertionError("did not raise")

def test_fun_with_extra_args():
    try:
        fun(1, 2)
    except TypeError:
        pass
    else:
        raise AssertionError("did not raise")

def test_fun_with_extra_kwargs():
    try:
        fun(x=1, y=2)
    except TypeError:
        pass
    else:
        raise AssertionError("did not raise")

