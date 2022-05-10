from _struct import Struct
s = Struct.__new__(Struct)
load_module('struct', s)
s.unpack_from('<bbbb', bytes([1, 2, 3, 4]))

#
# The buffer protocol
#
# Python has multiple implementations of strings and ustrings, some of which
# have the buffer protocol implemented and some of which don't.
#
# The selection of which strings/ustrings to define is based on the following
# criteria:
#
# 1) Must have the buffer protocol implemented
# 2) Preferably standard library modules
# 3) Stability, avoid deprecated modules or data types
#
# Note: this is one of those modules our "cross platform modules" check
# must be disabled for: http://trac.cython.org/cython_trac/wiki/CythonExtensions#PlatformSpecificExtensions
#

import string
from string import octdigits as string_octdigits
from string import ascii_letters as string_ascii_letters
from string import letters as string_letters
from string import hexdigits as string_hexdigits
from string import digits as string_digits
from string import
