import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
fun()

def test_compile_function_with_closure_2(space):
    def f(x):
        def g():
            return x
        return g
    code = compile(f(42), '<test>', 'exec')
    space.appexec([code], """(code):
        g = eval(code)
        assert g() == 42
    """)

def test_compile_function_with_closure_3(space):
    def f(x):
        def g():
            return x
        return g
    code = compile(f(42), '<test>', 'exec')
    space.appexec([code], """(code):
        g = eval(code)
        assert g() == 42
        assert g.func_closure[0].cell_contents == 42
    """)

def test_compile_function_with_closure_4(space):
    def f(x):
        def g():
            return x
        return g
    code = compile(f(42), '<test>', 'exec')
