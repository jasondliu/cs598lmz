import _struct
# Test _struct.Struct

# This test is used to check that the _struct module is working properly.
# It is not intended to be exhaustive.  Nor is it intended to test
# the speed or timing of the _struct module.  For timing tests,
# see test_timing.py.

import sys
import struct
import unittest
import _struct

from test import support

# The test data used in this module is NOT exhaustive.  It is intended
# to test the _struct module, and ensure that it gives the same results
# as the struct module.

# The format string used for test data
fmt = 'hhlLfd'

# The test data
data = [
    (1, 2, 3, 4, 5.0, 6.0),
    (-1, -2, -3, -4, -5.0, -6.0),
    (32767, -32768, 2147483647, -2147483648, 1e10, -1e10),
    ]

# The packed data corresponding to the test data
bdata = [
    b'\x
