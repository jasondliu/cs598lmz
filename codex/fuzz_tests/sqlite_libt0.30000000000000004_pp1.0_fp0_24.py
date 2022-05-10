import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import struct
import traceback

from ctypes import c_char_p, c_int, c_void_p, c_uint, c_ulong, c_char, c_ulonglong, c_longlong, c_size_t, c_long
from ctypes.wintypes import DWORD, HANDLE, BOOL, LPCVOID, LPVOID, LPCSTR, LPSTR, LPCWSTR, LPWSTR, WCHAR, ULONG, LPDWORD, BYTE, WORD, USHORT, LPBYTE, LPDWORD, LPWORD, LPULONG, LPLONG, LPUSHORT, LPBOOL, ULONGLONG, LONGLONG, ULONG64, LONG64, ULONG_PTR, LONG_PTR, DWORD_PTR, PVOID, LPVOID, SIZE_T, SSIZE_T, HANDLE, HMODULE, HINSTANCE, HLOCAL, HGLOBAL, HRSRC, HFILE, HWND, HGDIOBJ,
