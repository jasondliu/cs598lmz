from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')

'''
class Struct:
    def __init__(self, format):
        self.format = format

s = Struct('i')

'''

import unittest
from test.support import run_unittest

class StructTest(unittest.TestCase):

    def test_pack(self):
        self.assertEqual(s.pack(1), b'\x01\x00\x00\x00')
        self.assertEqual(s.pack(1, 2), b'\x01\x00\x00\x00\x02\x00\x00\x00')
        self.assertEqual(s.pack(1, 2, 3), b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00')
