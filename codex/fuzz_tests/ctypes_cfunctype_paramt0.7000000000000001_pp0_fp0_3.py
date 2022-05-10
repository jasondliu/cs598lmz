import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double)

def evaluate_difference_of_exponentials(k, x, y):
    return np.exp(-k*x) - np.exp(-k*y)

def evaluate_exponential_exponential(k, x, y):
    return np.exp(-k*x) * np.exp(-k*y)

def create_fun(f):
    """
    Create a ctypes function that can be passed to the C++ code.
    """
    def fun(x,y,z,k):
        return f(k, x, y)
    return FUNTYPE(fun)

def compute_integral(f, a, b, m, n, p, k_array):
    """
    Compute an integral of the form

        \int_a^b \int_a^b \int_a^b f(x,y,z,k) dx dy dz

    for some function f.

   
