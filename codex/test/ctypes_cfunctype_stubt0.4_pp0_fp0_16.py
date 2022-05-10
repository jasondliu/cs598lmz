import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_call_function():
    space = gettestobjspace(usemodules=('_cffi_backend',))
    w_fun = space.wrap(fun)
    assert space.eq_w(space.call_function(w_fun), space.wrap(42))

def test_call_function_with_args():
    space = gettestobjspace(usemodules=('_cffi_backend',))
    w_fun = space.wrap(fun)
    assert space.eq_w(space.call_function(w_fun, space.wrap(1),
                                          space.wrap(2)),
                       space.wrap(42))

def test_call_function_with_kwargs():
    space = gettestobjspace(usemodules=('_cffi_backend',))
    w_fun = space.wrap(fun)
