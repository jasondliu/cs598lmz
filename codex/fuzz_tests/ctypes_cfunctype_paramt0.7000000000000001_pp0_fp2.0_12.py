import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def wrap_function(lib, funcname, restype=ctypes.c_double, argtypes=[ctypes.c_double]):
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func

# use ctypes to load the shared object file

lib = ctypes.cdll.LoadLibrary('/home/tyler/Dropbox/projects/proj_functions/proj_functions_c/libproj_functions.so')

# wrap the c functions with python ctypes

func_interpolate = wrap_function(lib, 'interpolate')
func_interpolate_grad = wrap_function(lib, 'interpolate_grad')
func_interpolate_grad_grad = wrap_function(lib, 'interpolate_grad_grad')

func_delta = wrap_function(lib, 'delta')
func_delta_grad = wrap_function(lib, 'delta_
