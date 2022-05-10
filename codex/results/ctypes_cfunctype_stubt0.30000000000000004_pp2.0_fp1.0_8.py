import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_call():
    assert fun.__call__() == "hello"

def test_fun_call_kw():
    assert fun.__call__(a=1) == "hello"

def test_fun_call_kw_args():
    assert fun.__call__(a=1, *(1,2)) == "hello"

def test_fun_call_kw_args_kw():
    assert fun.__call__(a=1, *(1,2), **{'b':2}) == "hello"

def test_fun_call_args():
    assert fun.__call__(*(1,2)) == "hello"

def test_fun_call_args_kw():
    assert fun.__call__(*(1,2), **{'b':2}) == "hello"

def test_fun_call_kw_args_kw_args():
    assert fun.__call__(a=1, *(1,2),
