import _struct
# Test _struct.Struct.
#
# Test _struct.Struct, and therefore the _struct module, by comparing the
# results of packing and unpacking the structs defined in the module doc
# string with the expected results.

from test import support
import unittest
from test.support import bigmemtest
from test.support.script_helper import assert_python_ok

from _testcapi import INT_MAX

# The test values are all bytes objects, so that it is possible to compare
# the result of packing with the expected result.  The test values are
# chosen so that they can be represented exactly in the various formats.
#
# The test values for native packing are chosen so that the values are the
# same on all platforms.
#
# The test values for standard packing are chosen so that the values are
# the same on all platforms, and so that the values are the same as for
# native packing when the native format is the same as the standard
# format.
#
# The test values for byte order '>' and '<' are chosen so that they are
# the same as the native test values when the native byte order
