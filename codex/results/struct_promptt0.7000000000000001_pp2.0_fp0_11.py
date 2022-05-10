import _struct
# Test _struct.Struct
#
# This is tested in test_struct.
#
# The tests in test_struct_extra apply to the C API, not the Python API.
#
# The following tests are done in C:
# - constructor called with a non-str
# - constructor called with an str of incorrect length
# - constructor called with an invalid format string
# - incorrect format string used in pack/unpack/calcsize
# - pack/unpack called with an str of incorrect length
# - pack_into/unpack_from called with an str of incorrect length
#
# XXX(nnorwitz): We could add a test for passing tuple/list to pack.  It's
# kind of hard since there is some coercion.  Don't want to add a test for
# every possible permutation.

# Test pack_into/unpack_from.
# This can't be tested much in Python since the buffer API is not available.
# The test_struct_extra C tests do test this.

import _testcapi
import sys
import unittest
import struct
import array

class StructTestCase(unittest.
