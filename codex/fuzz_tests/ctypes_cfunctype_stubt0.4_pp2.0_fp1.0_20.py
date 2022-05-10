import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def fun_test():
    return fun()

def test_call_pyfunc_from_c():
    assert fun_test() == 1

def test_call_pyfunc_from_c_with_arg():
    def fun2(a):
        return a
    FUNTYPE2 = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
    fun2_c = FUNTYPE2(fun2)
    def fun_test2():
        return fun2_c(1)
    assert fun_test2() == 1

def test_call_pyfunc_from_c_with_kwarg():
    def fun3(a, b=1):
        return a, b
    FUNTYPE3 = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)
    fun3_c = FUNTYPE3(fun3)
    def fun_test3():
        return fun3_c(1)
    assert fun_test3() == (1
