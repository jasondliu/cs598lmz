import mmap
import os
import shutil
import subprocess
import sys
import tempfile
import time
import win32api
import win32con
import win32event
import win32file
import win32gui
import win32process
import win32security

from win32com.shell import shell, shellcon

import pywintypes

from ctypes import (
    Structure, c_ushort, c_ulong, c_uint, c_ulonglong, c_char, c_void_p,
    c_uint32, c_uint64, c_wchar_p, c_size_t, POINTER, byref, windll,
    create_unicode_buffer, create_string_buffer, sizeof, addressof
)

from ctypes.wintypes import (
    DWORD, LPCWSTR, LPWSTR, HANDLE, BOOL, WCHAR, WORD, BYTE, LPVOID, UINT,
    LPCVOID, INT, ULONG, LPBYTE, LPDWORD, LPBOOL, LPCSTR, LPSTR, LPCT
