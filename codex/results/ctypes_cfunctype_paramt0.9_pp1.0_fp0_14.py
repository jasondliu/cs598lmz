import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double, 
    ctypes.POINTER(ctypes.POINTER(ctypes.c_double)), ctypes.POINTER(ctypes.c_double))

@autojit
class BasePolynomial(object):
    '''Base class for a polynomial object'''
    def __init__(self, coefs, vars):
        '''Create a polynomial object with coefficients `coefs` and
        variables `vars`'''
        self.coefs = coefs
        self.vars = vars

        # Number of variables
        # if len(vars):
        #    self.nvars = len(vars[0])
        # else:
        #    self.nvars = 0

        self.nvars = len(vars)

        # Cache evaluations
        self.alleval = []

    def cp(self, coefs, nvars=None):
        '''Create a copy of this polynomial object with new coefficients'''
        p = type(self)(
