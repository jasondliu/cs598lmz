import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_exception_in_callback():
    import _testcapi
    try:
        _testcapi.raise_exception(fun, 42)
    except TypeError:
        pass
    else:
        assert False, "should have raised TypeError"

def test_exception_in_callback_2():
    import _testcapi
    try:
        _testcapi.raise_exception(fun, 42, 43)
    except TypeError:
        pass
    else:
        assert False, "should have raised TypeError"

def test_exception_in_callback_3():
    import _testcapi
    try:
        _testcapi.raise_exception(fun, 42, 43, 44)
    except TypeError:
        pass
    else:
        assert False, "should have raised TypeError"

def test_exception_in_callback_4():
    import _testcapi
    try:
        _testcapi.raise_exception(fun, 42, 43, 44, 45)
    except
