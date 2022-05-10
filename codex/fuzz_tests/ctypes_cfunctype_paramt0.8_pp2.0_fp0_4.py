import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_double),
                         ctypes.c_int, ctypes.c_void_p)

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

def myerror(code, msg):
    if code != 0:
        raise MyError(msg)


def set_gradient(func, n, extra_args=()):
    """
    Set the gradient function of a function.
    """

    def fprime(x, f, extra_args=()):
        func(x, f, g, extra_args)
    c_fprime = FUNTYPE(fprime)

    myerror.err_msg = ctypes.create_string_buffer('', 100)

    global f, g
    f = ctypes.c_double()
    g = ctypes.c_double * n

    check = ctypes.c_int(0)
    extra_args = tuple(extra_args)
    _set_gradient(c_fprime, ctypes.c_int(n
