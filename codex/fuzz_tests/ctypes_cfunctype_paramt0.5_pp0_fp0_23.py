import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def get_numpy_array_pointer(np_array):
    return np_array.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

def get_ctypes_array_pointer(ctypes_array):
    return ctypes.cast(ctypes_array, ctypes.POINTER(ctypes.c_double))

def wrap_function(lib, funcname, restype, argtypes):
    """Simplify wrapping ctypes functions"""
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func

def wrap_inplace_function(lib, funcname, argtypes):
    """Simplify wrapping ctypes functions that take inplace arguments"""
    func = lib.__getattr__(funcname)
    func.argtypes = argtypes
    return func

def wrap_inplace_func_args(func, *args):
    """Wrap
