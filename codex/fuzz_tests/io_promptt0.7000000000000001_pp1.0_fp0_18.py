import io
# Test io.RawIOBase.readinto()
# written by Mike C. Fletcher
# inspired by readinto() test in Lib/test/test_mmap.py

import unittest, os, mmap, io, tempfile, sys, stat

from support import TestFailed

class TestReadinto(unittest.TestCase):

    # Verify readinto() works as expected on an mmap.mmap object.
    # The mmap.mmap() object is created from a file that is opened
    # in binary (non-buffered) mode so that the expected data is not
    # altered by a buffer layer.
    def test_readinto(self):
        # Open a test file
        fname = tempfile.mktemp()
        f = open(fname, "w+b")
        try:
            # Write some test data to the file
            data = b"\x01\x02\x03\x04\x05\x06\x07\x08"
            f.write(data)
            f.flush()

            # Create an mmap object from the file
            # and
