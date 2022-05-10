import _struct
# Test _struct.Struct().format attribute.

import _struct
import unittest

class FormatTests(unittest.TestCase):

    def test_format(self):
        self.assertEqual(_struct.Struct('hhl').format, 'hhl')
        self.assertEqual(_struct.Struct('hhi').format, 'hhh')
        self.assertEqual(_struct.Struct('bBhHiIlLqQfd').format, 'bBhHiIlLqQfd')
        self.assertEqual(_struct.Struct('BHILfd').format, 'BBHHIILLf')
        self.assertEqual(_struct.Struct('BHILfd').format, 'BBHHIILLf')
        self.assertEqual(_struct.Struct('xxxx').format, 'xxxx')
        self.assertEqual(_struct.Struct('bxxh').format, 'bxxh')
        self.assertEqual(_struct.Struct('ccc').format, 'ccc')
        self.assertEqual(_struct.Struct('cccc').format, 'cccc')
        self.assertEqual
