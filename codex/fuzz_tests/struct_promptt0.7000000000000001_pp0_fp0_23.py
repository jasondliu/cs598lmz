import _struct
# Test _struct.Struct objects for ability to pack.

import unittest
from test import test_support
from StringIO import StringIO

class StructTestCase(unittest.TestCase):
    def test_unpack(self):
        tests = [('hhl', (1, 2, 3), '\x01\x00\x02\x00\x03\x00\x00\x00'),
                 ('hhl', (-1, -2, -3), '\xff\xff\xfe\xff\xfd\xff\xff\xff'),
                 ('hhhh', (1, 2, 3, 4), '\x01\x00\x02\x00\x03\x00\x04\x00'),
                 ('bhi', (1, 2, 3), '\x01\x02\x00\x00\x03\x00\x00\x00'),
                 ('bhi', (1, -2, 3), '\x01\xfe\xff\xff\x03\x00\x00\x00'),
                 ('bli', (1, 2, 3
