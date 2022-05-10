import _struct
# Test _struct.Struct

# Test the basic methods

import _struct
import unittest
from test import support

class StructTest(unittest.TestCase):

    def test_format(self):
        self.assertEqual(_struct.Struct('cbhilfd').format, 'cbhilfd')
        self.assertEqual(_struct.Struct('cbhilfdP').format, 'cbhilfdP')
        self.assertEqual(_struct.Struct('cbhilfdP').size, _struct.calcsize('cbhilfdP'))
        self.assertEqual(_struct.Struct('cbhilfdP').format_size, _struct.calcsize('cbhilfdP'))
        self.assertEqual(_struct.Struct('cbhilfdP').format_size, _struct.calcsize('cbhilfdP'))
        self.assertEqual(_struct.Struct('cbhilfdP').format_size, _struct.calcsize('cbhilfdP'))
