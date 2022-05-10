import ctypes
# Test ctypes.CFUNCTYPE with restype = None
from ctypes import *
from ctypes import wintypes
from ctypes.wintypes import *

PROCESS_TERMINATE = 1
STILL_ACTIVE = 259

kernel32 = windll.kernel32
CloseHandle = kernel32.CloseHandle
OpenProcess = kernel32.OpenProcess

def get_proc_pidbyname(procname):
    PROCESS_ALL_ACCESS = 0x000F0000 | 0x00100000 | 0xFFF
    hwnd = user32.FindWindowW(None, from_buffer(create_string_buffer(procname)))
    if hwnd == 0:
        return 0
    else:
        lpdwProcessId = (wintypes.DWORD * 1)()
        user32.GetWindowThreadProcessId(hwnd, lpdwProcessId)
        hProcess = OpenProcess(PROCESS_ALL_ACCESS, False, lpdwProcessId[0])
        return hProcess


def proc_getname(hwnd):
    _GetWindowTextLength = windll.user
