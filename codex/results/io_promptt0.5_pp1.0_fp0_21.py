import io
# Test io.RawIOBase().

import io
import os
import sys
import unittest
import tempfile
import weakref

# Needed on Windows because the file is opened with
# FILE_SHARE_DELETE.
if sys.platform == 'win32':
    import msvcrt

# A mixin for testing RawIOBase objects.

class BaseTestRawIO(object):

    def test_basic(self):
        # test a simple input file
        f = self.open(self.TEST_FILE, 'rb')
        got = f.read()
        f.close()
        self.assertEqual(got, self.TEST_FILE_CONTENTS)

    def test_read_into(self):
        # test a simple input file
        f = self.open(self.TEST_FILE, 'rb')
        b = bytearray(len(self.TEST_FILE_CONTENTS))
        n = f.readinto(b)
        f.close()
        self.assertEqual(b, self.TEST_FILE_CONTENTS)
        self.
