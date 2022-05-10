import _struct
# Test _struct.Struct class.

import unittest
from test import test_support
from _testcapi import getargs_b, getargs_B, getargs_h, getargs_H, getargs_i, \
     getargs_I, getargs_l, getargs_L, getargs_q, getargs_Q, getargs_f, \
     getargs_d, getargs_P, getargs_c, getargs_s, getargs_p, getargs_z

# Old-style formatting of structs, which cannot be packed natively.
# The tests are skipped on big-endian platforms.
# The struct module supports only little-endian formats.
native_alignment = _struct.calcsize('=i')
if (native_alignment == 4) and (__byteorder__ == "little"):
    test_old_struct = True
else:
    test_old_struct = False

