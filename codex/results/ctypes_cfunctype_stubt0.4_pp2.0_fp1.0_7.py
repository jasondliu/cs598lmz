import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

def return_zero():
    return 0

def return_zero_inline():
    return 0

def return_zero_inline_with_arg(arg):
    return 0

def return_zero_inline_with_args(arg1, arg2):
    return 0

def return_zero_inline_with_args_and_kwargs(arg1, arg2, kwarg1=None, kwarg2=None):
    return 0

def return_zero_inline_with_args_and_kwargs_and_defaults(arg1, arg2, kwarg1=None, kwarg2=None, default1=None, default2=None):
    return 0

def return_zero_inline_with_args_and_kwargs_and_defaults_and_varargs(*args, **kwargs):
    return 0

def return_zero_inline_with_args_and_kwargs_and_defaults_and_varargs_and_kwonly(*args, kwonly=None, **kwargs):
    return 0
