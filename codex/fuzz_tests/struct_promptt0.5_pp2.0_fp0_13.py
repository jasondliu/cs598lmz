import _struct
# Test _struct.Struct

import _struct
import sys
import unittest


class StructTestCase(unittest.TestCase):

    def test_format(self):
        # test the format string parsing
        self.assertEqual(_struct.Struct('x').format, 'x')
        self.assertEqual(_struct.Struct('cb').format, 'cb')
        self.assertEqual(_struct.Struct('10c').format, '10c')
        self.assertEqual(_struct.Struct('10c').size, 10)
        self.assertEqual(_struct.Struct('10c').alignment, 1)
        self.assertEqual(_struct.Struct('10cx').format, '10cx')
        self.assertEqual(_struct.Struct('10cx').size, 11)
        self.assertEqual(_struct.Struct('10cx').alignment, 1)
        self.assertEqual(_struct.Struct('10cx12c').format, '10cx12c')
        self.assertEqual(_struct.Struct('10cx12c').size, 23)

