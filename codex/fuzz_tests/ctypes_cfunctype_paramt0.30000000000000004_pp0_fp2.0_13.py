import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_function(f):
    return FUNTYPE(f)

def make_function_from_string(s):
    return make_function(eval(s))

def make_function_from_file(fname):
    with open(fname) as f:
        return make_function(eval(f.read()))

def make_function_from_file_and_arguments(fname, *args):
    with open(fname) as f:
        return make_function(eval(f.read()))(*args)

def make_function_from_file_and_arguments_and_kwargs(fname, *args, **kwargs):
    with open(fname) as f:
        return make_function(eval(f.read()))(*args, **kwargs)

def make_function_from_file_and_kwargs(fname, **kwargs):
    with open(fname) as f:
        return make_function(eval(f.read()))
