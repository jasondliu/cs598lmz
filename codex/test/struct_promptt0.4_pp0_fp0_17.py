import _struct
# Test _struct.Struct.

# This test is not exhaustive, but it does cover the most common
# cases.  The format character set is limited to those supported
# by the native platform.

import sys
import unittest
from test import support

# Define native size, alignment and format.
native_sizes = {'c': 1, 'b': 1, 'B': 1, '?': 1,
                'h': 2, 'H': 2, 'i': 4, 'I': 4,
                'l': 4, 'L': 4, 'q': 8, 'Q': 8,
                'f': 4, 'd': 8, 'P': 4, 'n': 2, 'N': 4}
