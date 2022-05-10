import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

class C(object):
    @FUNTYPE
    def fun(self):
        return 42

def f():
    x = FUNTYPE(lambda: 42)
    return x()

print fun()
print C().fun()
print f()
""")

    def test_c_function_type_with_defaults(self):
        self.run_test("""
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.c_int, ctypes.c_int)
@FUNTYPE
def fun(a, b=42):
    return a+b

def f():
    x = FUNTYPE(lambda a, b=42: a+b)
    return x(1)

print fun(1)
print f()
""")

    def test_c_function_type_with_kwargs(self):
        self.run_test("""
import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.c_int, ctypes.
