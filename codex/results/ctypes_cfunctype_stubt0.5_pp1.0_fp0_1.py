import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_cfunc():
    f = fun(1)
    assert f() == 1

def test_cfunc_callback():
    @FUNTYPE
    def g(x):
        return x + 1
    assert g(1) == 2

def test_cfunc_callback_2():
    def h(x):
        return x + 1
    h = FUNTYPE(h)
    assert h(1) == 2

def test_cfunc_callback_3():
    def h(x):
        return x + 1
    h = FUNTYPE(h)
    h(1)
    assert h(1) == 2

def test_cfunc_callback_4():
    def h(x):
        return x + 1
    h = FUNTYPE(h)
    h(1)
    h(1)
    assert h(1) == 2

def test_cfunc_callback_5():
    def h(x):
        return x + 1
    h = FUNTYPE(h)
    h(1)
    h(1
