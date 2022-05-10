import _struct
# Test _struct.Struct

import sys
sys.path.insert(0, "..")

from test import support
from test.support import bigmemtest
import struct
from struct import Struct
from struct import pack, unpack
from struct import calcsize
from struct import error
import array
from array import array as Array
from ctypes import *
from operator import mul
from functools import reduce

from test import test_support

# This string is used as a seed for some tests, to make it easier to find
# bugs.  It's not a real number, and it's binary, not hex, so the
# string-to-float and string-to-double conversions work differently in
# big- and little-endian machines.
nasty_number_as_string = b'\x9a\x7d\xfd\xfd\xfd\xfd\xfd\xfd'

# a list of (fmt, number) to test all the standard integer formats
integer_codes = [('b', -127), ('B', 255), ('h', -32767), ('H', 65535),
                 ('
