import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_type():
    assert type(fun) == FUNTYPE

def test_fun_type_repr():
    assert repr(FUNTYPE) == "&lt;class 'ctypes.CFUNCTYPE(object)&gt;
</code>

