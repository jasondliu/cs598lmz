import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def register_fun(lib, func, funtype=FUNTYPE):
    """register function into c library"""
    cfunc = funtype(func)
    cfunc.argtypes = None
    cfunc.restype = ctypes.c_int
    setattr(lib, func.__name__, cfunc)
    return func

class FileStream(object):
    """
    file stream class

    >>> fs = FileStream(filename)
    >>> print fs.read()
    """
    def __init__(self, filename, cache_max=1024):
        self.filename = filename
        self.cache_max = cache_max
        self.cache = bytes()
        self.cursor = 0
        self.lib = ctypes.cdll.LoadLibrary('./libstream.so')
        #register c functions
        register_fun(self.lib, self.has_next)
        register_fun(self.lib, self.next_ch)
        register_fun(self.lib, self.read)
