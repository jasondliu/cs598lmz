import ctypes
import ctypes.util
import threading
import sqlite3
import subprocess
import os
from sys import platform
import etw

VIRTUAL_MACHINE = (platform == 'win32' and ctypes.windll.kernel32.IsWow64Process(ctypes.windll.kernel32.GetCurrentProcess(), ctypes.byref(ctypes.c_long())))

#
# There are two mechanisms to get command line args under NT.
# One is converting those from unicode to ascii
# The other is getting a pointer to the full unicode command line arguments
#

if VIRTUAL_MACHINE:
    commandLineW = ctypes.cast(
        ctypes.cast(
            ctypes.windll.kernel32.GetCommandLineW(), 
            ctypes.POINTER(ctypes.c_void_p)
        ).contents.value, 
        ctypes.c_wchar_p
    ).value
    # get the command line arguments
