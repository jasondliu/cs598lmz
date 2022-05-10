import ctypes
# Test ctypes.CField.from_address
#
# This tests that a CField can be created from an address and that it
# has the correct value.
#
# It also tests that the type of the field is the same as the type of
# the CField.
#
# It also tests that a CField can be created from an address, and then
# that address can be accessed from the CField to ensure that the
# address is correct.
#
# It also tests that the address of a CField can be used to create
# another CField, and that the value of that CField is correct.

import sys
import ctypes
from ctypes import util
from ctypes.test import need_symbol

if sys.platform == 'win32':
    libc_name = util.find_msvcrt()
else:
    libc_name = None

# A simple structure
class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

# A structure with a nested structure
class T(ctypes
