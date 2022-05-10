import ctypes
# Test ctypes.CFUNCTYPE.
# Test

def errorCheck(result, func, args):
    if result is 0:
        err = ctypes.get_errno()
        raise OSError(err, "Last win32 error: %s, in function %r with arguments %r" % (ctypes.FormatError(err), func.__name__, args))
#   err = ctypes.get_last_error()
#   if hasattr(errno, 'errorcode'):
#       err = errno.errorcode[err]
#   else:
#       err = ctypes.FormatError(err).strip()
#   if err:
#       raise OSError, err
    return args

LPWSTR = ctypes.c_wchar_p
BOOL = ctypes.c_long
LONG = ctypes.c_long
HKEY = ctypes.c_void_p
PHKEY = ctypes.c_void_p
PVOID = ctypes.c_void_p
DWORD = ctypes.c_ulong
