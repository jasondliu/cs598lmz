import _struct
# Test _struct.Struct.

import unittest
from test import support

class StructTest(unittest.TestCase):
    def test_struct(self):
        # Test some standard sized and aligned structs.
        tests = [
                ('bb', 1, 2, b'\x01\x02'),
                ('bh', 1, 2, b'\x01\x00\x02\x00'),
                ('b', 1, b'\x01'),
                ('h', 1, b'\x00\x01'),
                ('i', 1, b'\x00\x00\x00\x01'),
                ('l', 1, b'\x00\x00\x00\x00\x00\x00\x00\x01'),
                ('q', 1, b'\x00\x00\x00\x00\x00\x00\x00\x00\x01'),
                ('f', 1, b'\x00\x00\x80?'),
                ('d', 1, b'\x00\x00\x00\x00
