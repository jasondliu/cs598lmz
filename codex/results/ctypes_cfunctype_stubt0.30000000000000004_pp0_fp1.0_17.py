import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_call_function():
    assert fun() == "hello"

def test_call_function_with_arguments():
    def func(a, b):
        return a + b
    func_type = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)
    func_ptr = func_type(func)
    assert func_ptr(1, 2) == 3

def test_call_function_with_kwargs():
    def func(a, b):
        return a + b
    func_type = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)
    func_ptr = func_type(func)
    assert func_ptr(b=2, a=1) == 3

def test_call_function_with_varargs():
    def func(*args):
        return sum(args)
    func_type = ctypes.CFUNCTYPE(ctypes.py_
