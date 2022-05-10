import _struct
# Test _struct.Struct with all supported types and alignment requirements

import warnings
import _testcapi
from test import support
from test.test_support import bigaddrspacetest, run_unittest
from test.support import run_with_tz
from test import string_tests

# Output values for each format character.  Each list contains
# one or more values to be used in packing, followed by the
# expected output from packing that value.  If an entry contains
# more than one input value, they all have the same output.

