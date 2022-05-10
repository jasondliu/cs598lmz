import _struct
# Test _struct.Struct.

import sys
import unittest
from test import support

# A list of struct formats to test.
formats = [
    'x', 'c', 'b', 'B', '?', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd',
    's', 'p', 'P'
]

# A list of values corresponding to the formats above.
values = [
    b'x', b'x', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0.0, b'x', 0, 0
]

# A list of struct format strings which should raise struct.error
bad_formats = [
    'z', '', 'P#', 'abcdefghij', 'ccccccccccccccccccccccccccccccccccccccccc'
]

# A list of struct format strings which should raise struct.error
# when used with '@' alignment.
bad_formats_with_alignment
