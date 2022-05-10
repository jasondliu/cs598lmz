import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def is_null(fun):
    return not bool(ctypes.addressof(fun))

def test_fun():
    fun_ = fun()
    fun2 = fun
    assert not is_null(fun_)
    assert not is_null(fun2)
    fun = None
    assert is_null(fun_)
    assert not is_null(fun2)
    del fun2
    assert is_null(fun_)

def test_freefun():
    fun_ = fun()
    fun2 = fun
    assert not is_null(fun_)
    assert not is_null(fun2)
    lltype.free(fun, flavor='raw')
    assert is_null(fun_)
    assert not is_null(fun2)
    lltype.free(fun2, flavor='raw')
    assert is_null(fun_)

def test_free_null():
    fun = None
    lltype.free(fun, flavor='raw')
    # does not crash

def test_free_null_with_
