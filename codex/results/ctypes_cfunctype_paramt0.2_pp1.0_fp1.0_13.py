import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def make_func(func):
    return FUNTYPE(func)

def make_func_from_string(func_string):
    return make_func(eval(func_string))

def make_func_from_file(filename):
    with open(filename, 'r') as f:
        func_string = f.read()
    return make_func(eval(func_string))

def make_func_from_file_with_name(filename, func_name):
    with open(filename, 'r') as f:
        func_string = f.read()
    return make_func(eval(func_string + '.' + func_name))

def make_func_from_file_with_name_and_args(filename, func_name, *args):
    with open(filename, 'r') as f:
        func_string = f.read()
    return make_func(eval(func_string + '.' + func_name)(*args))

def make_func_from_
