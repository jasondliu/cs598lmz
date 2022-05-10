import ctypes
# Test ctypes.CFUNCTYPE
#
#
#

import _ctypes_test

try:
    import _ctypes
except ImportError:
    pass
else:
    try:
        _ctypes.dlopen
    except AttributeError:
        pass
    else:
        import sys
        if sys.platform == "win32":
            from ctypes import windll
            from ctypes.wintypes import HWND, UINT, WPARAM, LPARAM, LRESULT
            from ctypes import CFUNCTYPE, c_int, c_void_p, c_long
            prototype = CFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)
            paramflags = (1, "hwnd", 0), (1, "message", 0), (1, "wParam", 0), (1, "lParam", 0)
            MessageBox = prototype(("MessageBoxA", windll.user32), paramflags)
            MessageBox.__doc__ = "MessageBoxA function"

            class WNDPROC(prototype):
                pass

           
