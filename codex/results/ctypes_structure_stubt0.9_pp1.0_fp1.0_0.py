import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p.in_dll(ctypes, "wrong_name")

try:
    S()
except AttributeError as detail:
    print(detail)

# Loading a function from a DLL is similar.  The access is via the in_dll()
# attribute of a function class created with _FuncPtr().
#
# This example uses the CreateFile() function in kernel32.dll, to open a file
# on disk
#

from ctypes import *
from ctypes.wintypes import *

kernel32 = WinDLL("kernel32", use_last_error=True)

_CreateFile = windll.kernel32.CreateFileA
_CreateFile.argtypes = [LPCSTR, DWORD, DWORD, c_void_p, DWORD, DWORD, HANDLE]
_CreateFile.restype = HANDLE

dwDesiredAccess = GENERIC_READ
dwShareMode = 0
lpSecurityAttributes = None
dwCreationDisposition = OPEN_EXISTING
dwFlagsAndAttributes = FILE_AT
