import _struct
# Test _struct.Struct
import unittest
from test import support

import struct

class SizesAndAlignments(unittest.TestCase):
    def setUp(self):
        # alignment values for std. ABIs (Mac, x86{,_64}, ARM, PPC{,64})
        self.alignment = {'x': 1, 'c': 1, 'b': 1, 'B': 1, '?': 1,
                          'h': 2, 'H': 2, 'i': 4, 'I': 4, 'l': 4, 'L': 4,
                          'q': 8, 'Q': 8, 'f': 4, 'd': 8, 's': 1, 'p': 1,
                          'P': 4}
        self.size = {'x': 1, 'c': 1, 'b': 1, 'B': 1, '?': 1,
                     'h': 2, 'H': 2, 'i': 4, 'I': 4, 'l': 4, 'L': 4,
                     'q': 8, 'Q': 8, 'f': 4,
