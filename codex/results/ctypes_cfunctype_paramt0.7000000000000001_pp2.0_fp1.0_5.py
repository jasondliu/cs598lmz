import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

def error_check(result, func, args):
    if result != 0:
        errno = ctypes.get_errno()
        raise OSError(errno, os.strerror(errno))
    return args

#: Error checking callback.
error_check_callback = ctypes.CFUNCTYPE(None, ctypes.c_int, FUNTYPE, ctypes.py_object)

#: Error checking callback used by default.
check_error_callback = error_check_callback(error_check)

#: Default callback used by libev.
default_callback = check_error_callback

#: Default event loop.
default_loop = None

#: Default timeout.
default_timeout = 1.0


__all__ = [
    'default_callback', 'default_loop', 'default_timeout',
    'error_check_callback', 'check_error_callback'
]
