import _struct
# Test _struct.Struct for creating and manipulating Struct instances.

import test.support
import platform
import sys
import unittest

class StructTestCase(unittest.TestCase):

    # Tests for individual struct format characters are in test_structseq.py

    def test_unpack(self):
        # Check that _struct.unpack with a unicode format string decodes
        # byte strings passed as arguments.
        args = (b'\xff',)
        if sys.version_info < (3,):
            expect = (255,)
        else:
            expect = (b'\xff',)
        self.assertEqual(_struct.unpack(str(b'B'), args[0]), expect)
        self.assertEqual(_struct.unpack(str(b'B'), *args), expect)

    def test_calcsize(self):
        # Check that _struct.calcsize with a unicode format string decodes
        # byte strings passed as arguments.
        self.assertEqual(_struct.calcsize(str(b'B')), 1)
        self.assertEqual
