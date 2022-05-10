import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

# Test the ctypes.c_void_p type
print ctypes.c_void_p.from_param(ctypes.c_void_p(42))

# Test the ctypes.wintypes module
from ctypes import wintypes
for tp in (wintypes.BOOL,
           wintypes.BYTE,
           wintypes.CHAR,
           wintypes.WCHAR,
           wintypes.SHORT,
           wintypes.USHORT,
           wintypes.INT,
           wintypes.UINT,
           wintypes.LONG,
           wintypes.ULONG,
           wintypes.LONGLONG,
           wintypes.ULONGLONG,
           wintypes.FLOAT,
           wintypes.DOUBLE,
           wintypes.POINTER(wintypes.INT),
           wintypes.HANDLE,
           wintypes.HWND,
           wintypes.LPARAM,
           wintypes.WPARAM
