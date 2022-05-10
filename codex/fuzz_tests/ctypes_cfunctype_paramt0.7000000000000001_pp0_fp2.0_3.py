import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def wrap_function(lib, name, restype=ctypes.c_double, argtypes=(ctypes.c_double,)):
    func = lib.__getattr__(name)
    func.restype = restype
    func.argtypes = argtypes
    return func

def wrap_function_c(lib, name, restype=ctypes.c_double, argtypes=(ctypes.c_double,)):
    func = lib.__getattr__(name)
    func.restype = restype
    func.argtypes = argtypes
    return func

def wrap_function_f(lib, name, restype=ctypes.c_float, argtypes=(ctypes.c_float,)):
    func = lib.__getattr__(name)
    func.restype = restype
    func.argtypes = argtypes
    return func

def wrap_function_cf(lib, name, restype=ctypes.c_double, argtypes=(ctypes.c_float,)):
   
