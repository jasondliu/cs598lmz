import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42

def test_fun_exception():
    try:
        fun(1)
    except TypeError:
        pass
    else:
        raise AssertionError("should have raised")

def test_fun_exception_2():
    try:
        fun(1, 2)
    except TypeError:
        pass
    else:
        raise AssertionError("should have raised")

def test_fun_exception_3():
    try:
        fun(1, 2, 3)
    except TypeError:
        pass
    else:
        raise AssertionError("should have raised")

def test_fun_exception_4():
    try:
        fun(1, 2, 3, 4)
    except TypeError:
        pass
    else:
        raise AssertionError("should have raised")

def test_fun_exception_5():
    try:
        fun(1, 2, 3, 4, 5)
    except TypeError:
        pass

