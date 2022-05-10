import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)

def wrap_function(lib, funcname, restype=ctypes.c_double, argtypes=[ctypes.c_double]):
    """ Simplify wrapping ctypes functions """
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func

# load the shared object file
lib = ctypes.cdll.LoadLibrary('./libcalc.so')

# wrap the C function
c_cosine = wrap_function(lib, 'cosine')

# call the C function
print('cosine(2.0) = ' + str(c_cosine(2.0)))

# wrap the C function
c_sine = wrap_function(lib, 'sine')

# call the C function
print('sine(2.0) = ' + str(c_sine(2.0)))

# wrap the C function
c_tangent = wrap_function(lib, 'tangent')

