import ctypes
# Test ctypes.CField.
from ctypes.test import need_symbol

if need_symbol('c_wchar'):
    from ctypes import c_wchar, c_wchar_p, c_ushort, Structure
    class X(Structure):
        _fields_ = [("a", c_wchar),
                    ("b", c_wchar * 3),
                    ("c", c_wchar * 4),
                    ("d", c_wchar * 5),
                    ("e", c_wchar * 6),
                    ("f", c_wchar * 7),
                    ("g", c_wchar * 8),
                    ("h", c_wchar * 9),
                    ("i", c_wchar * 10),
                    ("j", c_wchar * 11),
                    ("k", c_wchar * 12),
                    ("l", c_wchar * 13),
                    ("m", c_wchar * 14),
                    ("n", c_wchar * 15),
                    ("o", c_wchar * 16),
                    ("p", c_wchar * 32)]

    if
