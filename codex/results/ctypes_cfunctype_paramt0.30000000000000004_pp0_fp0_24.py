import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def wrap_function(lib, funcname, restype=ctypes.c_double, argtypes=[ctypes.c_double]):
    """ Simplify wrapping ctypes functions """
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func

def wrap_function_as_ufunc(lib, funcname, restype=ctypes.c_double, argtypes=[ctypes.c_double]):
    """ Wrap ctypes function as a numpy ufunc """
    func = wrap_function(lib, funcname, restype, argtypes)
    return np.frompyfunc(func, len(argtypes), 1)

# Load the library
lib = ctypes.cdll.LoadLibrary('./libmylib.so')

# Wrap the functions
my_sin = wrap_function(lib, 'my_sin')
my_cos = wrap_function(lib, 'my_cos')
my_tan = wrap_function(
