import ctypes
ctypes.cast(None, ctypes.c_void_p)

import ctypes.wintypes

from ctypes import windll
from ctypes.wintypes import HWND, HANDLE, DWORD, WORD, BOOL, UINT, LONG, LPARAM, WPARAM

from ctypes import byref, Structure, Union, POINTER, pointer, sizeof

from ctypes import c_char_p, c_wchar_p, c_void_p, c_int, c_long, c_size_t, c_ubyte, c_ushort

from ctypes import CFUNCTYPE, WINFUNCTYPE, WINFUNCTYPE as WINFUNCTYPE_

import ctypes.util

from ctypes import addressof

from ctypes import create_string_buffer, create_unicode_buffer

from ctypes import memmove

from ctypes import sizeof as ctypes_sizeof

from ctypes import string_at, wstring_at

from ctypes import cast as ctypes_cast

from ctypes import byref as ctypes
