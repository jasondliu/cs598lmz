import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_call_function():
    space = gettestobjspace(usemodules=('_cffi_backend',))
    w_res = space.appexec([space.wrap(fun)], """(fun):
        import _cffi_backend
        return _cffi_backend.call_function(fun)
    """)
    assert space.str_w(w_res) == "hello"

def test_call_function_with_struct():
    space = gettestobjspace(usemodules=('_cffi_backend',))
    w_res = space.appexec([space.wrap(fun)], """(fun):
        import _cffi_backend
        return _cffi_backend.call_function(fun, 'struct(x=1, y=2)')
    """)
    assert space.str_w(w_res) == "hello"

