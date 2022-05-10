import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def get_errno(failures):
    """Get detailed information about the last error."""
    buf = ctypes.create_string_buffer(128)
    libc = ctypes.CDLL(None)
    libc.strerror_r(failures.errno, buf, 127)
    return buf.value

def errcheck(result, func, args):
    """Check the return value of the function called."""
    if result != 0:
        raise OSError(get_errno(result), 'got result %d from %s' %
                      (result, func.__name__))
    return result

class result_t(ctypes.Structure):
    _fields_ = [("failed", ctypes.c_int)]

class gg_function(FUNTYPE):
    def __init__(self, func):
        FUNTYPE.__init__(self, errcheck)
        self.func = func
    def __call__(self, *args):
        return self.func(*
