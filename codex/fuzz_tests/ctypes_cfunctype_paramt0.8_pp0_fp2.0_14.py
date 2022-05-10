import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int, ctypes.POINTER(ctypes.c_double))

@FUNTYPE
def f(n, x):
    """ Objective function """
    return numpy.sum(x * x)

@FUNTYPE
def g0(n, x):
    """ Gradient of objective function """
    ret = numpy.empty(n)
    ret.fill(2.0)
    return ret

@FUNTYPE
def h0(n, x, new_x):
    """ Hessian of objective function """
    ret = numpy.empty(n)
    ret.fill(2.0)
    return ret

def g(n, x, user_data):
    """ Constraint function """
    return numpy.array([1.0 - numpy.sum(x), 0.5 - numpy.sum(x ** 2)], dtype=numpy.float64)

def jac_g(n, x, new_x, user_data):
    """ Jacobian of constraints """
    return numpy.
