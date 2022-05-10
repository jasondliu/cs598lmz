import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_float)

def call_func(func, *args):
    return func(*args)

def make_func(name, address):
    return FUNTYPE(address)

def make_callback(func, argtypes, restype=None):
    return FUNTYPE(func)

def convert_args(args):
    return args

def convert_result(res):
    return res

def external(name, args, result):
    return name

def dlopen(name):
    return name

def dlsym(lib, name):
    return name

def dlclose(lib):
    pass

def get_errno():
    return 0

def set_errno(n):
    pass

def get_last_error():
    return 0

def set_last_error(n):
    pass
