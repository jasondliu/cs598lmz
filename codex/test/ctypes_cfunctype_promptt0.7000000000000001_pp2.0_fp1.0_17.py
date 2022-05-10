import ctypes
# Test ctypes.CFUNCTYPE
if ctypes.sizeof(ctypes.c_int) == 4:
    WPARAM = ctypes.c_uint32
    LPARAM = ctypes.c_int32
else:
    WPARAM = ctypes.c_ulong
    LPARAM = ctypes.c_long

LRESULT = ctypes.c_long
HWND = ctypes.c_void_p
UINT = ctypes.c_uint
WM_USER = 1024

# Test byref()
