import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_call_function():
    space = gettestobjspace(usemodules=('_cffi_backend',))
    w_fun = space.wrap(fun)
    w_result = space.call_function(w_fun)
    assert space.str_w(w_result) == "hello"
    w_result = space.call_function(w_fun, w_fun)
    assert space.str_w(w_result) == "hello"
    w_result = space.call_function(w_fun, w_fun, w_fun)
    assert space.str_w(w_result) == "hello"
    w_result = space.call_function(w_fun, w_fun, w_fun, w_fun)
    assert space.str_w(w_result) == "hello"
    w_result = space.call_function(w_fun, w_fun, w_fun, w_fun, w_fun)
    assert space.str_w(w_result) == "hello"
   
