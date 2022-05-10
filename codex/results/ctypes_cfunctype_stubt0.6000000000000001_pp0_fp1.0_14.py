import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def f():
    return fun()

def g():
    return f()

def h():
    return g()

def test_call_chain():
    res = h()
    assert res == 1

def test_call_chain_direct():
    res = fun()
    assert res == 1
