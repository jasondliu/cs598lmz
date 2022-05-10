import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_function_type():
    assert fun() == 1
    assert type(fun) is FUNTYPE

def test_function_type_call():
    @FUNTYPE
    def fun2(x):
        return x + 1
    assert fun2(1) == 2
    assert fun2(1.5) == 2.5

def test_function_type_call_with_struct():
    class S(ctypes.Structure):
        _fields_ = [("x", ctypes.c_int)]
    @FUNTYPE
    def fun3(s):
        return s.x + 1
    assert fun3(S(1)) == 2

def test_function_type_call_with_struct_pointer():
    class S(ctypes.Structure):
        _fields_ = [("x", ctypes.c_int)]
    @FUNTYPE
    def fun4(s):
        return s.contents.x + 1
    assert fun4(ctypes.pointer(S(1))) == 2

