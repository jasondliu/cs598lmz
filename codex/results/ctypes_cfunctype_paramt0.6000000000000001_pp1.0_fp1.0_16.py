import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int)

def _make_function(function, ndim):
    def f(x, gradient, n):
        if gradient is None:
            return function(x[:ndim])
        else:
            return function(x[:ndim], gradient[:ndim])
    return FUNTYPE(f)

class Function(object):
    def __init__(self, function, ndim):
        self.function = _make_function(function, ndim)
        self.ndim = ndim

    def __call__(self, x, gradient=None):
        return self.function(x, gradient, self.ndim)

class Rosenbrock(object):

    def __init__(self):
        self.function = Function(self.f, 2)

    def __call__(self, x, gradient = None):
        return self.f(x, gradient)

    def f(self, x,
