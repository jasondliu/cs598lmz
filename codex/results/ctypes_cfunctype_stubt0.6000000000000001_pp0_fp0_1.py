import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello world"

descr = get_descr(fun)
assert descr is not None

compiled = compile_loop([], descr, FUNTYPE.TO)
res = compiled()
assert res == "Hello world"

def my_compile_loop(f, descr, policy):
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
    compiled = compile_loop([], descr, FUNTYPE.TO)
    def wrapper():
        res = compiled()
        assert res == "Hello world"
        return res
    return wrapper

def f():
    my_compile_loop(fun, descr, FUNTYPE.TO)()

t = TranslationContext()
t.buildannotator().build_types(f, [])
t.buildrtyper().specialize()
t.checkgraphs()

t.compile_c()

import py
py.test.skip("the test below is not correct")
import test_ll_os
test_ll_os.ll_to_string(t.compiled
