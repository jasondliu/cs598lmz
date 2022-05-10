import ctypes
# Test ctypes.CFUNCTYPE with a function that returns a pointer to a function.

# Uses the stdcall convention, because it's a Win32 convention and it's
# cleaner to use the same convention on all platforms.

import ctypes
from ctypes import wintypes

user32 = ctypes.windll.user32

HWND = wintypes.HWND
HMENU = wintypes.HMENU

GetSystemMenu = user32.GetSystemMenu
GetSystemMenu.argtypes = [HWND, wintypes.BOOL]
GetSystemMenu.restype = HMENU

CFUNCTYPE = ctypes.CFUNCTYPE
systemmenu_callback_type = CFUNCTYPE(HMENU, HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM)

SetWindowLong = user32.SetWindowLongW
SetWindowLong.argtypes = [HWND, wintypes.INT, systemmenu_callback_type]
SetWindowLong.restype = systemmenu_callback_type

oldWndPro
