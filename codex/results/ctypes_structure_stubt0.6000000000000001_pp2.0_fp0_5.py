import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p.in_dll(ctypes.pythonapi, 'PyExc_ValueError')

s = S()
print(s.x)

import os
import ctypes
from ctypes import wintypes

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

kernel32.GetModuleHandleW.restype = wintypes.HMODULE
kernel32.GetModuleHandleW.argtypes = [wintypes.LPCWSTR]

kernel32.GetProcAddress.restype = wintypes.FARPROC
kernel32.GetProcAddress.argtypes = [wintypes.HMODULE, wintypes.LPCSTR]

kernel32.CloseHandle.argtypes = [wintypes.HANDLE]

# Get a handle to the DLL
hdll = kernel32.GetModuleHandleW(None)

# Get the address of PyExc_ValueError
exc_address = kernel32.GetProcAddress(hdll, b'PyExc_ValueError')
print(hex(
