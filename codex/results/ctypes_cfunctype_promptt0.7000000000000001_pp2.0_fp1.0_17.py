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
SendMessage = ctypes.windll.user32.SendMessageA
SendMessage.argtypes = [HWND, UINT, WPARAM, LPARAM]
SendMessage.restype = LRESULT

# Test byvalue()
SetWindowLong = ctypes.windll.user32.SetWindowLongA
SetWindowLong.argtypes = [HWND, ctypes.c_int, ctypes.c_long]
SetWindowLong.restype = ctypes.c_long
GWL_WNDPROC = -4


class WNDPROC(ct
