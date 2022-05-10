import ctypes
# Test ctypes.CFUNCTYPE
if sys.platform == 'win32':
    from ctypes import wintypes
    prototype = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.UINT,
                                   wintypes.WPARAM, wintypes.LPARAM)
    parameters = (1, "hwnd", 0), (1, "uMsg", 0), (1, "wParam", 0), (1, "lParam", 0)
else:
    prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p)
    parameters = (1, "fd", 0), (1, "event", 0), (1, "arg", 0)

def func(*args):
    print args

CMPFUNC = prototype(func)

# Test ctypes.PYFUNCTYPE
PYFUNC = ctypes.PYFUNCTYPE(ctypes.c_int, ctypes.py_object, ctypes.
