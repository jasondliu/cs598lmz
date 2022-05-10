import _struct
# Test _struct.Struct.

import unittest
import sys
import io

class StructTest(unittest.TestCase):
    def test_format_size(self):
        self.assertEqual(_struct.calcsize(b""), 0)
        self.assertEqual(_struct.calcsize(b"<"), 0)
        self.assertEqual(_struct.calcsize(b"<b"), 1)
        self.assertEqual(_struct.calcsize(b"<bB"), 2)
        self.assertEqual(_struct.calcsize(b"<bBh"), 4)
        self.assertEqual(_struct.calcsize(b"<bBhL"), 8)
        self.assertEqual(_struct.calcsize(b"<bBhLq"), 16)
        self.assertEqual(_struct.calcsize(b"<bBhLqQ"), 16)

    def test_pack(self):
        self.assertEqual(_struct.pack(b"", ()), b"")
        self.assertEqual(_struct.
