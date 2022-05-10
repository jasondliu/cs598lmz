import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_fun():
    assert fun() == 42

def test_fun_call():
    assert fun(1, 2, 3) == 42
    assert fun(1, 2, 3, 4) == 42
    assert fun(1, 2, 3, 4, 5) == 42
    assert fun(1, 2, 3, 4, 5, 6) == 42
    assert fun(1, 2, 3, 4, 5, 6, 7) == 42
    assert fun(1, 2, 3, 4, 5, 6, 7, 8) == 42
    assert fun(1, 2, 3, 4, 5, 6, 7, 8, 9) == 42
    assert fun(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 42
    assert fun(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11) == 42
    assert fun(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) == 42
