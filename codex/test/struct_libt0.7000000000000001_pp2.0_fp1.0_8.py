import _struct

class _tls_dtor(ctypes.Structure):
    _fields_ = [
        ('next', ctypes.c_void_p),
        ('func', ctypes.c_void_p),
        ('arg', ctypes.c_void_p),
        ('dso_handle', ctypes.c_void_p),
    ]

class TLS(object):
    __slots__ = ['__weakref__']

    def __init__(self):
        self.__dict__["__keygen"] = None
        self.__dict__["__dict"] = None

    def __getattr__(self, attr):
        ctx = getattr(threading.current_thread(), '_tls_ctx_', None)
        if ctx is None:
            raise AttributeError("'_tls_ctx_' not found")
        if not attr in ctx:
            raise AttributeError("'%s' not found" % attr)
        return ctx[attr]

