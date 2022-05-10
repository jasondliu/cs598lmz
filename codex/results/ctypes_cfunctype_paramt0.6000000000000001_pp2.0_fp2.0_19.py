import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

import sys
if sys.platform == 'win32':
    from ctypes import windll
    from ctypes.wintypes import HWND, UINT, WPARAM, LPARAM, LRESULT
    prototype = WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)
    paramflags = (1, "hwnd"), (1, "msg"), (1, "wparam"), (1, "lparam")

else:
    from ctypes import cdll
    from ctypes import c_int
    prototype = CFUNCTYPE(c_int, c_int, c_int, c_int, c_int)
    paramflags = (1, "w"), (1, "u"), (1, "id"), (1, "hwnd"), (1, "hwndInsertAfter"), (1, "x"), (1, "y"), (1, "cx"), (1, "cy"), (1, "flags")


class _
