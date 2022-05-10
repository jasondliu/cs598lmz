import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_void_p)

def interfunc(fun):
    """It is a wrapper that takes a Python function and converts it to a C function 
    pointer type that can be used with C functions that require a C callback function"""
    def wrapper(x, n, params):
        return fun(x, n, params)
    return FUNTYPE(wrapper)

def wrap_interfunc(fun):
    """It is a wrapper for interfunc.  It is called by the user in place of interfunc"""
    return interfunc(fun)

###########################################################################################################################################

# from scipy.optimize import minimize
# from scipy.optimize import basinhopping

###########################################################################################################################################

# def simplex(x, n, params):
    # """This function is used in the scipy.optimize.minimize routines"""
    # func = params
    # return func(x)

# def minimize(func, x0, method
