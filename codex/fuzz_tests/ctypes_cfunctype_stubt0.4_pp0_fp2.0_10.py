import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"

def test_fun():
    assert fun() == "fun"

@FUNTYPE
def fun_arg(arg):
    return arg

def test_fun_arg():
    assert fun_arg(42) == 42

@FUNTYPE
def fun_arg_kw(arg, kw=23):
    return arg, kw

def test_fun_arg_kw():
    assert fun_arg_kw(42) == (42, 23)
    assert fun_arg_kw(42, kw=24) == (42, 24)

@FUNTYPE
def fun_arg_kw_var(arg, kw=23, *args):
    return arg, kw, args

def test_fun_arg_kw_var():
    assert fun_arg_kw_var(42) == (42, 23, ())
    assert fun_arg_kw_var(42, kw=24) == (42, 24, ())
    assert fun_arg_kw_var(42, kw=24, *(1, 2, 3)) == (
