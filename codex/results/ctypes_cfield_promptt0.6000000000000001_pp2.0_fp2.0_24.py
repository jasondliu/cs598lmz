import ctypes
# Test ctypes.CField.from_param()
from ctypes.test import is_resource_enabled
ctypes.CField.from_param(42, ctypes.c_int)
ctypes.CField.from_param(42, ctypes.c_void_p)
ctypes.CField.from_param(42, ctypes.c_char_p)
ctypes.CField.from_param(42, ctypes.c_wchar_p)
ctypes.CField.from_param(42, ctypes.c_ulong)
ctypes.CField.from_param(42, ctypes.c_ulonglong)
ctypes.CField.from_param(ctypes.c_char_p(42), ctypes.c_char_p)
ctypes.CField.from_param(ctypes.c_wchar_p(42), ctypes.c_wchar_p)
ctypes.CField.from_param(ctypes.c_void_p(42), ctypes.c_void_p)
ctypes.CField.from_param(ctypes.
