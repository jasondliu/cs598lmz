import ctypes
import ctypes.util
import threading
import sqlite3
import re

from ctypes import c_char, c_char_p, c_long, c_ulong, c_int, c_void_p, c_double, byref
from ctypes.wintypes import DWORD, HWND, RECT, LPARAM, UINT_PTR, MSG, BOOL, VOID, LPCSTR
from rctk.apps.foregroundwindow import ForegroundWindow

import logging
log = logging.getLogger('rctk.win32')

class Win32Error(Exception):
    pass

def check_error(result, func, args):
    """
    Call Win32 GetLastError() and raise a Win32Error exception.
    """
    if result == 0:
        raise Win32Error(ctypes.FormatError())
    else:
        return result

