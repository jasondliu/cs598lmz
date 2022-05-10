import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_cfuntype():
    assert fun() == 42

def test_cfuntype_callable():
    class C:
        f = fun
    assert C().f() == 42

