import ctypes
# Test ctypes.CFUNCTYPE
from ctypes.test import need_symbol
paramflags = (1, "", "", "", 5, 0, 8)
have_al = True
try:
    ctypes.windll.kernel32
except AttributeError:
    have_al = False
if have_al:
    windll = ctypes.cdll.LoadLibrary(ctypes.util.find_msvcrt())
    GetCommandLineA = windll.GetCommandLineA
    GetCommandLineA.argtypes = ()
    # If this function were in kernel32.dll, we could just do
    # GetCommandLineA.restype = ctypes.c_char_p
    # Since it's in msvcrt, we have to do
    GetCommandLineA.restype = ctypes.c_void_p
    try:
        GetCommandLineA()
    except WindowsError:
        # this is raised on Win9x, because the function wasn't found
        have_al = False
import unittest
from operator import itemgetter
TK_INT = 1
TK_SHORT
