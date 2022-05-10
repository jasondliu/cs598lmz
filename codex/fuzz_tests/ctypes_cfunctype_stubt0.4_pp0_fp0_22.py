import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def test_fun():
    assert fun() is None

def test_fun_exception():
    def g():
        raise ValueError
    f = FUNTYPE(g)
    raises(ValueError, f)

def test_fun_exception_reraised():
    def g():
        raise ValueError
    f = FUNTYPE(g)
    try:
        f()
    except ValueError:
        pass
    else:
        assert False, "exception not raised"

def test_fun_exception_reraised_2():
    def g():
        raise ValueError
    f = FUNTYPE(g)
    try:
        f()
    except ValueError:
        pass
    else:
        assert False, "exception not raised"
    try:
        f()
    except ValueError:
        pass
    else:
        assert False, "exception not raised"

def test_fun_exception_reraised_3():
    def g():
        raise ValueError
    f = FUNTYPE(g)
    try:
