import mmap
# Test mmap.mmap()
import os
import subprocess
import sys
import unittest
import warnings

# Is 64-bit windows?
import test.support
is_64bit_windows = (sys.platform == "win32" and
                    sys.maxsize > 2**32)

if sys.platform != 'win32':
    import fcntl
    import resource
    import termios
    import tty

# This is used solely to test the creation of bytes objects.
class P(object):
    def __bytes__(self):
        return b"I am bytes"

class AutoFileTests(unittest.TestCase):
    def setUp(self):
        self.f = io.BytesIO(b"some initial text data")

    def test_attributes(self):
        f = self.f
        self.assertTrue(f.closed)
        self.assertEqual(f.mode, "wb")
        self.assertEqual(f.name, None)
        self.assertEqual(f.buffer, f)
        self.assertEqual(f.
