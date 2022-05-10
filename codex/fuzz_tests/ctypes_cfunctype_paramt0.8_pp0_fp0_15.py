import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    ctypes.c_double, ctypes.c_int, np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")
)
def cost_fn_wrapper(fun):
    def converted_fun(n, x):
        x = np.array(x)
        return fun(x)
    return FUNTYPE(converted_fun)

lib = ctypes.CDLL('./libhyperopt.so')

lib.pso_minimize.argtypes = [cost_fn_wrapper, ctypes.c_int, ctypes.c_int, np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"), ctypes.c_double, ctypes.c_int]
lib.pso_minimize.restype = np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")

def pso_minimize(fun, dim, lb=-5, ub=5, n_particles=50, n_iter=100):

