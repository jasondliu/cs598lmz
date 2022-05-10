import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_function_type():
    assert fun() == 1

def test_function_type_call():
    assert FUNTYPE(fun)() == 1

def test_function_type_call_with_args():
    assert FUNTYPE(fun)(1, 2, 3) == 1

def test_function_type_call_with_kwargs():
    assert FUNTYPE(fun)(a=1, b=2, c=3) == 1

def test_function_type_call_with_args_and_kwargs():
    assert FUNTYPE(fun)(1, 2, 3, a=1, b=2, c=3) == 1

def test_function_type_call_with_args_and_kwargs_and_star():
    assert FUNTYPE(fun)(1, 2, 3, a=1, b=2, c=3, *(4, 5, 6)) == 1

