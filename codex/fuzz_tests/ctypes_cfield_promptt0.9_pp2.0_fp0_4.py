import ctypes
# Test ctypes.CField
import datetime
import _ctypes_test
import os
import sys
import unittest
from test.test_support import run_unittest
from ctypes import (Structure, Union, Array, POINTER, pointer,
                    byref, sizeof, addressof,
                    get_errno, set_errno, WinError,
                    create_string_buffer, c_buffer, c_wchar_p, c_void_p,
                    CFUNCTYPE, PythonAPI, cdll, c_char_p,
                    c_char, c_wchar, c_ubyte, c_short, c_ushort, c_int,
                    c_uint, c_longlong, c_ulonglong, c_float, c_double,
                    c_long, c_ulong, c_bool, c_uint8, c_int8, c_uint16,
                    c_int16, c_int32, c_uint32, c_int64, c_uint64,
                    c_size_t)
from ctypes.test import is_resource_enabled
