import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def _make_callback(func, arg):
    """
    Create a C callback function from a Python function
    """
    @FUNTYPE
    def _callback(*args):
        func(arg)
    return _callback

def _make_callback_ex(func, arg):
    """
    Create a C callback function from a Python function
    """
    @FUNTYPE
    def _callback(*args):
        func(*arg)
    return _callback

class _Callback:
    def __init__(self, func, arg):
        self.func = func
        self.arg = arg
        self.cfunc = _make_callback(func, arg)

class _CallbackEx:
    def __init__(self, func, arg):
        self.func = func
        self.arg = arg
        self.cfunc = _make_callback_ex(func, arg)

class _CallbackList:
    def __init__(self):
        self.callbacks = []

    def __call__(self, *args):
        for cb in self.
