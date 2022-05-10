import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,
                           ctypes.c_double,
                           ctypes.c_double,
                           ctypes.c_double,
                           ctypes.c_double,
                           ctypes.c_double,
                           ctypes.c_double,
                           ctypes.c_double,
                           ctypes.c_double,
                           ctypes.c_double,
                           ctypes.c_double,
                           ctypes.c_double,
                           ctypes.c_double,
                           ctypes.c_double)

# load the library, using numpy flags
_lib = np.ctypeslib.load_library('lib', '.')

# setup the return types and argument types
_lib.calc_evals.restype = None
_lib.calc_evals.argtypes = [FUNTYPE, ctypes.c_int,
                            np.ctypeslib.ndpointer(np.float64, flags="C_CONTIGUOUS"),
                            np.ctypeslib.ndpointer(np.float64, flags="
