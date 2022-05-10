import ctypes
# Test ctypes.CField

if sys.platform not in ('win32',):
    raise ImportError, "CField not supported on this platform"

import _ctypes_test

class COpaque(ctypes.c_void_p):
    _type_ = "h"

class CTest(ctypes.Structure):
    _fields_ = [("field1", ctypes.c_char_p),
                ("field2", ctypes.c_int),
                # Here's an explicitly sized pointer field
                ("field3", ctypes.CField(ctypes.c_short, "field2", 1)),
                ("field4", ctypes.CField(COpaque, "field1", 2)),
                ]

class CTest2(ctypes.Structure):
    _fields_ = [("field1", ctypes.c_char_p),
                ("field2", ctypes.CField(COpaque, "field1", 1)),
                ("field3", ctypes.CField(COpaque, "field2", 0)),
                ]

class CTest3(ctypes.
