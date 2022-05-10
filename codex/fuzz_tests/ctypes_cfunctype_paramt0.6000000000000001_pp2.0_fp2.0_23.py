import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

# =============================================================================
#
# =============================================================================
class C_Callable(object):
    """
    A C callable is a C function that can be called from Python.
    """
    def __init__(self, callback_name, c_type, c_func, c_func_args):
        self.callback_name = callback_name
        self.c_type = c_type
        self.c_func = c_func
        self.c_func_args = c_func_args

    def __call__(self, *args, **kwargs):
        self.c_func(*args, **kwargs)


# =============================================================================
#
# =============================================================================
class C_Callback(object):
    """
    A C callback is a function that is called from C.
    """
    def __init__(self, callback_name, c_type, callback_func, callback_func_args):
        self.callback_name = callback_name
        self.c_type = c_type
        self.callback_func = callback_func
        self.callback_
