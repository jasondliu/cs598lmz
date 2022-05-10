import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_function(f):
    return FUNTYPE(f)

def make_function_from_string(s):
    return make_function(eval(s))

def make_function_from_file(fname):
    with open(fname) as f:
        return make_function(eval(f.read()))

def make_function_from_file_with_name(fname):
    with open(fname) as f:
        return make_function(eval(f.read()))

def make_function_from_file_with_name(fname, name):
    with open(fname) as f:
        return make_function(eval(f.read()))

def make_function_from_file_with_name(fname, name):
    with open(fname) as f:
        return make_function(eval(f.read()))

def make_function_from_file_with_name(fname, name):
    with open(fname)
