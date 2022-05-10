import ctypes
import ctypes.util
import threading
import sqlite3
import sys

# Main executable
__main_executable__ = sys.executable

# Resources for Windows
if sys.platform == 'win32':
    import win32con
    import win32api
    import win32security
    __has_win32api__ = True
    __has_win32security__ = True
else: # Unix-like OS (including Linux, macOS, etc)
    __has_win32api__ = False
    __has_win32security__ = False

# Function prototypes
LPCTSTR = ctypes.c_char_p # LPCTSTR = 'L'ong 'P'ointer to a 'C'onstant 'T'ype 'S'tring
LPVOID = ctypes.c_void_p # LPVOID = 'L'ong 'P'ointer to a 'VO'id type
DWORD = ctypes.c_ulong # DWORD = 'D'ouble 'WORD' (size is 32-bit)

# OpenProcess
__kernel32__ = ctypes.windll.kernel32

__OpenProcess__ = __kernel32
