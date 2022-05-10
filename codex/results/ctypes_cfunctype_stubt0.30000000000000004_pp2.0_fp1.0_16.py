import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_call_function():
    space = gettestobjspace(usemodules=('cppyy',))
    w_res = space.appexec([], """():
        import cppyy
        return cppyy.gbl.fun()""")
    assert space.str_w(w_res) == "hello"

def test_call_function_with_args():
    space = gettestobjspace(usemodules=('cppyy',))
    w_res = space.appexec([], """():
        import cppyy
        return cppyy.gbl.fun_with_args(1, 2)""")
    assert space.int_w(w_res) == 3

def test_call_function_with_default_args():
    space = gettestobjspace(usemodules=('cppyy',))
    w_res = space.appexec([], """():
        import cppyy
        return cppyy.gbl.fun_with_default_args(1)""")
    assert space.int
