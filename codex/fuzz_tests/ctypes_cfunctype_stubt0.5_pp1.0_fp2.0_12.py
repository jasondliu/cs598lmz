import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun_type():
    assert fun() == 1

def test_fun_type_call():
    assert fun.__call__() == 1

def test_fun_type_call_with_args():
    raises(TypeError, fun.__call__, 1)

def test_fun_type_call_with_kwargs():
    raises(TypeError, fun.__call__, x=1)

@FUNTYPE
def fun_arg(arg):
    return arg + 1

def test_fun_type_arg():
    assert fun_arg(1) == 2

def test_fun_type_arg_call():
    assert fun_arg.__call__(1) == 2

def test_fun_type_arg_call_with_args():
    raises(TypeError, fun_arg.__call__, 1, 2)

def test_fun_type_arg_call_with_kwargs():
    raises(TypeError, fun_arg.__call__, 1, x=1)

@FUNTYPE
def
