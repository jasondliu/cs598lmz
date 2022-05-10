import ctypes
import ctypes.util
import threading
import sqlite3
import struct
import datetime
import locale

_winreg = ctypes.windll.advapi32
_winreg.RegOpenKeyExW.argtypes = [
        HKEY,
        LPCWSTR,
        DWORD,
        REGSAM,
        ctypes.POINTER(HKEY)]
_winreg.RegOpenKeyExW.restype = LONG
_winreg.RegQueryValueExW.argtypes = [
        HKEY,
        LPCWSTR,
        LPDWORD,
        LPDWORD,
        LPVOID,
        LPDWORD]
_winreg.RegEnumValueW.argtypes = [
        HKEY,
        DWORD,
        LPWSTR,
        LPDWORD,
        LPDWORD,
        LPDWORD,
        LPBYTE,
        LPDWORD]

# Helper functions
def _parseFreeSpace(string):
    try:
        value, units = string.split()
        value = float(value)
        units = units.lower()
       
