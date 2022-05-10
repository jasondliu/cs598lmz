import ctypes
# Test ctypes.CFUNCTYPE and ctypes.POINTER
import _ctypes_test

import _opcode
import unittest

function_pointer = ctypes._CFuncPtr
l = [_ctypes_test.LP_c_char,
     _ctypes_test.LP_c_short,
     _ctypes_test.LP_c_ushort,
     _ctypes_test.LP_c_long,
     _ctypes_test.LP_c_ulong,
     _ctypes_test.LP_c_ulonglong,
     _ctypes_test.LP_c_longlong,
     _ctypes_test.LP_c_wchar_p,
     _ctypes_test.LP_c_void_p,
     _ctypes_test.LP_c_char_p,
     _ctypes_test.LP_c_double,
     _ctypes_test.LP_c_float]

def _initialize(self, *args):
    # Called before action()
    self._sum = 0

def _finalize(self, index):
