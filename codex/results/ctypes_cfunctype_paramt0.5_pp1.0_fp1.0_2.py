import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def wrap_function(lib, funcname, restype=ctypes.c_double, argtypes=None, errcheck=None):
    """Simplify wrapping ctypes functions"""
    func = lib.__getattr__(funcname)
    func.restype = restype
    if argtypes:
        func.argtypes = argtypes
    if errcheck:
        func.errcheck = errcheck
    return func

def load_library(libname, loader_path):
    """Load a library"""
    from ctypes.util import find_library
    from ctypes import CDLL
    libpath = find_library(libname)
    if libpath is None:
        libpath = os.path.join(loader_path, libname)
    return CDLL(libpath)

class Cached(object):
    """A descriptor that caches the result of a method"""
    def __init__(self, method):
        self.method = method
        self.name = method.__name__
        self.
