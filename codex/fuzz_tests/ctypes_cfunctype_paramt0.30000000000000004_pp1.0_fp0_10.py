import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)

class _Callback(object):
    def __init__(self, func, data):
        self.func = FUNTYPE(func)
        self.data = data

    def __call__(self, *args):
        self.func(self.data)

def _as_parameter_ (self):
    # see ctypes docs for why we need to do this
    return self

def _set_functions(self):
    self.set_callback = self.lib.g_source_set_callback
    self.set_callback.argtypes = [ctypes.c_void_p, FUNTYPE, ctypes.c_void_p]
    self.set_callback.restype = None

    self.attach = self.lib.g_source_attach
    self.attach.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    self.attach.restype = ctypes.c_uint

    self.destroy = self.lib.g_source
