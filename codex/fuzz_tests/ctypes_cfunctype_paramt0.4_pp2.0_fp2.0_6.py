import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def get_function(lib, name):
    func = getattr(lib, name)
    func.argtypes = (ctypes.c_int, ctypes.c_int)
    func.restype = ctypes.c_int
    return func

def get_function_c(lib, name):
    func = getattr(lib, name)
    func.argtypes = (ctypes.c_int, ctypes.c_int)
    func.restype = ctypes.c_int
    return func

def get_function_f(lib, name):
    func = getattr(lib, name)
    func.argtypes = (ctypes.c_int, ctypes.c_int)
    func.restype = ctypes.c_int
    return func

def get_function_py(lib, name):
    func = getattr(lib, name)
    func.argtypes = (ctypes.c_int, ctypes.c_int)

