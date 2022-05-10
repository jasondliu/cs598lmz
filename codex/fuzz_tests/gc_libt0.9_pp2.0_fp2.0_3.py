import gc, weakref, ctypes
from platform import system
if system() != 'Windows':
    raise SystemError("Cannot use this Python module on non Windows systems!")

from ctypes.wintypes import HWND, INT, HINSTANCE
from msvcrt import get_osfhandle
from win32api import GetConsoleWindow
from win32gui import FindWindowW, FindWindowExW

MSG = c_int
WNDPROC = WINFUNCTYPE(INT, HWND, MSG, INT, INT)

user32 = windll.user32
kernel32 = windll.kernel32
kernel32.GetStdHandle.argtypes = [INT]
kernel32.GetStdHandle.restype = c_void_p

STD_ERROR_HANDLE = -12
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11

# INVALID_HANDLE_VALUE = -1
INPUT_RECORD = wintypes._INPUT_RECORD
PINPUT_RECORD = POINTER(INPUT_RECORD)
L
