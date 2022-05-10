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

pack_functions = [
    (
        "B",
        [0, 127, 255],
        [b"\000", b"\177", b"\377"]
    ),
    (
        "b",
        [0, 127, 128, 255, -128, -129, -1],
        [b"\000", b"\177", b"\200", b"\377", b"\200", b"\201", b"\377"]
    ),
    (
        "H",
        [0, 32767, 65535],
        [b"
