import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

def get_func(lib, name, args, restype=ctypes.c_int):
    func = getattr(lib, name)
    func.argtypes = args
    func.restype = restype
    return func

def get_func_errcheck(lib, name, args, restype=ctypes.c_int):
    func = getattr(lib, name)
    func.argtypes = args
    func.restype = restype
    func.errcheck = ctypes.pythonapi.PyErr_CheckSignals
    return func

def get_func_errcheck_type(lib, name, args, restype=ctypes.c_int):
    func = getattr(lib, name)
    func.argtypes = args
    func.restype = restype
    func.errcheck = ctypes.pythonapi.PyErr_CheckSignals
    return FUNTYPE(func)

def get_func_type(lib, name, args, restype=ctypes.c_int):
    func = getattr
