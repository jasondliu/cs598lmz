import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)

def c_function(f):
    return FUNTYPE(f)

if __name__ == "__main__":
    import sys
    from scipy.integrate.quadpack import quad
    from scipy.integrate.quadpack import _quadpack
    from scipy.integrate.quadpack import _test_multivariate_function
    from scipy.integrate.quadpack import _test_function
    from scipy.integrate.quadpack import _test_multivariate_function_2
    from scipy.integrate.quadpack import _test_function_2
    from scipy.integrate.quadpack import _test_function_3
    from scipy.integrate.quadpack import _test_function_4
    from scipy.integrate.quadpack import _test_function_5
    from scipy.integrate.quadpack import _test_function_6
    from scipy.integrate.quadpack import _test_function_7
    from scip
