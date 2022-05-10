import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

def test_cfunc(f):
    return f(1, 2)

def test_cfunc_with_defaults(f, a=1, b=2):
    return f(a, b)

def test_cfunc_with_kwargs(f, a=1, b=2):
    return f(a, b)

def test_cfunc_with_kwargs_and_defaults(f, a=1, b=2):
    return f(a, b)

def test_cfunc_with_kwargs_and_defaults_and_args(f, a=1, b=2, *args):
    return f(a, b)

def test_cfunc_with_kwargs_and_defaults_and_args_and_kwargs(f, a=1, b=2, *args, **kwargs):
    return f(a, b)

def test_cfunc_with_kwargs_and_defaults_and_args_and_kwargs_and_varargs
