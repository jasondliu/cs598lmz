import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

def c_function():
    return ctypes.c_double(4711)

def c_function_with_wrong_signature():
    return 42

def c_function_with_args(a, b=None):
    if a == 1 and b == 2:
        return ctypes.c_double(4711)
    return 42

def c_function_with_varargs(a, *args):
    if a == 1 and args == (2,3):
        return ctypes.c_double(4711)
    return 42

def c_function_with_kwargs(a, **kwargs):
    if a == 1 and kwargs == {'c': 3, 'b': 2}:
        return ctypes.c_double(4711)
    return 42

def c_function_with_args_and_varargs(a, b, *args):
    if a == 1 and b == 2 and args == (3,4):
        return ctypes.c_double(4711)
    return 42


