import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_call_function():
    space = gettestobjspace(usemodules=('cppyy',))
    w_res = space.appexec([space.wrap(fun)], """(fun):
        import cppyy
        cppyy.gbl.gInterpreter.Declare("int f() { return fun(); }")
        return cppyy.gbl.f()
    """)
    assert space.int_w(w_res) == 1

def test_call_function_with_args():
    space = gettestobjspace(usemodules=('cppyy',))
    w_res = space.appexec([space.wrap(fun)], """(fun):
        import cppyy
        cppyy.gbl.gInterpreter.Declare("int f(int x) { return x+fun(); }")
        return cppyy.gbl.f(3)
    """)
    assert space.int_w(w_res) == 4

def test_call_function_with_args_and_kwds
