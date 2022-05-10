import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def get_function(lib, name, restype=ctypes.c_int, argtypes=()):
    func = lib.__getattr__(name)
    func.restype = restype
    func.argtypes = argtypes
    return func

def get_function_safe(lib, name, restype=ctypes.c_int, argtypes=()):
    try:
        return get_function(lib, name, restype, argtypes)
    except AttributeError:
        return None

def get_functions(lib, names, restype=ctypes.c_int, argtypes=()):
    return [get_function(lib, name, restype, argtypes) for name in names]

def get_functions_safe(lib, names, restype=ctypes.c_int, argtypes=()):
    return [get_function_safe(lib, name, restype, argtypes) for name in names]

def get_functions_with_prefix(lib, prefix,
