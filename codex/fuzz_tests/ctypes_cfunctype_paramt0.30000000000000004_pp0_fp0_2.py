import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def get_libc():
    libc = ctypes.CDLL(None)
    return libc

def get_function(libc, name, restype=None, argtypes=None):
    func = getattr(libc, name)
    func.restype = restype
    func.argtypes = argtypes
    return func

def get_signal(libc, signum):
    return get_function(libc, 'signal', FUNTYPE, [ctypes.c_int, FUNTYPE])

def get_raise(libc):
    return get_function(libc, 'raise', None, [ctypes.c_int])

def get_kill(libc):
    return get_function(libc, 'kill', None, [ctypes.c_int, ctypes.c_int])

def get_getpid(libc):
    return get_function(libc, 'getpid', ctypes.c_int, None)

def get_fork(libc):
