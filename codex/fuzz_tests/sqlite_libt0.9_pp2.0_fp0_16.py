import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import json

def GetTopProcPath(pid):
    """
    Return the path of the executable of the process
    """
    if sys.platform == 'win32':
        # In windows CreateToolhelp32Snapshot must be called before using pid
        hProcessSnap = ctypes.windll.kernel32.CreateToolhelp32Snapshot(
            ctypes.c_int(0x00000002), ctypes.c_int(pid))

        if hProcessSnap == -1:
            raise ctypes.WinError()

        pe32 = PROCESSENTRY32()
        pe32.dwSize = ctypes.sizeof(PROCESSENTRY32)

        ctypes.windll.kernel32.Process32First(
            ctypes.c_void_p(hProcessSnap), ctypes.byref(pe32))
        ctypes.windll.kernel32.Process32Next(
            ctypes.c_void_p(hProcessSnap), ctypes.byref(pe32))

        return pe32.szExeFile
    else:
        return
