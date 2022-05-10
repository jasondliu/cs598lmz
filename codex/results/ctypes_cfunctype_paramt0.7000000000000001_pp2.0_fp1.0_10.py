import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_float)

def get_jacobian_func(func):
    def func_wrapper(*args):
        y = func(*args)
        y = np.asarray(y, dtype=np.float32)
        jac = [autograd.jacobian(lambda x: func(x, *args[1:]), x) for x in args]
        return y, jac
    return func_wrapper


def get_function(func):
    def func_wrapper(*args):
        y = func(*args)
        y = np.asarray(y, dtype=np.float32)
        return y
    return func_wrapper


class Function(object):
    def __init__(self, func):
        self.func = func
        self.func_wrapper = get_jacobian_func(func)
        self.jac = None
        self.y = None

    def __call__(self, *args):
        y, jac = self.func_wrapper(*args)
        self.jac = jac
        self.y
