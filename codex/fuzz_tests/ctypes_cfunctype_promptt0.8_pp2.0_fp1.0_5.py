import ctypes
# Test ctypes.CFUNCTYPE()
from ctypes import *
from ctypes.test import need_symbol
from time import sleep

from ctypes import (c_int, c_uint, c_char, c_double, c_short, c_ushort,
                    c_longlong, c_ulonglong, c_char_p, c_float, create_string_buffer,
                    c_ubyte, c_bool, c_longdouble, c_wchar, c_wchar_p)

from _ctypes_test import (callback_i, callback_f, callback_d, callback_r,
                          callback_b, callback_B, callback_h, callback_H,
                          callback_i_ii, callback_p, callback_p_p, callback_P,
                          callback_P_P, callback_ii, callback_dd, callback_ff,
                          callback_bb, callback_hh, callback_i_p_p, callback_C,
                          callback_S, callback_i_s, callback_s_s,
                          callback_S_S, callback_
