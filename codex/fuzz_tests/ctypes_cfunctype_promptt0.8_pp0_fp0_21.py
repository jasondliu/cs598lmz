import ctypes
# Test ctypes.CFUNCTYPE
import ctypes.util

from ctypes import *

# XXX test pointer -> pointer conversion


if os.name == "nt":
    windll.kernel32.GetLastError.restype = c_ulong
    windll.kernel32.GetLastError.argtypes = []
    def GetLastError():
        """call GetLastError(), and return the resulting error code"""
        return windll.kernel32.GetLastError()

    def WinError(code=None, descr=None):
        """WinError(code) -> exception
        WinError(descr) -> exception

        Create a Windows error exception. The argument may specify either an
        error code (defaults to GetLastError()), or a descriptive string.
        """
        if code is None:
            code = GetLastError()
        if descr is None:
            descr = FormatError(code)
        exc = WindowsError(code, descr)
        exc.strerror = descr
        return exc

    FORMAT_MESSAGE_FROM_SYSTEM = 0x00001000

    def Format
