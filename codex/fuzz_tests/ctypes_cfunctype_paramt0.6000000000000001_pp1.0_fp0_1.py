import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int32, ctypes.c_char_p)
def fun_from_c(c_func, restype=None, argtypes=None, errcheck=None):
    """Wraps a ctypes function as a python function."""
    if restype is None:
        restype = ctypes.c_int32
    if argtypes is None:
        argtypes = (ctypes.c_char_p,)

    def wrapped_c_func(*args, **kwargs):
        if not isinstance(args, tuple):
            args = tuple(args)
        c_args = []
        for a in args:
            if isinstance(a, str):
                c_args.append(ctypes.c_char_p(a.encode('utf-8')))
            else:
                c_args.append(a)
        return c_func(*c_args, **kwargs)

    fun = FUNTYPE(c_func)
    fun.argtypes = argtypes
    fun.restype = restype
    if errcheck is not None:

