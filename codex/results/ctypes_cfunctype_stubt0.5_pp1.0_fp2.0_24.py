import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_function_type():
    f = fun
    assert f() == 1

def test_function_type_instance():
    f = fun()
    assert f() == 1

def test_function_type_instance_call():
    f = fun()
    assert f.__call__() == 1

def test_function_type_instance_call_args():
    f = fun()
    assert f.__call__(1, 2, 3) == 1

def test_function_type_instance_call_kwargs():
    f = fun()
    assert f.__call__(a=1, b=2, c=3) == 1

def test_function_type_instance_call_args_kwargs():
    f = fun()
    assert f.__call__(1, 2, 3, a=1, b=2, c=3) == 1

def test_function_type_instance_call_args_kwargs_starargs():
    f = fun()
    assert f.__call__(1, 2, 3
