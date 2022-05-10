import lzma
# Test LZMADecompressor
#
# This test is a bit different from the others.  It is not
# a test of the module's correctness, but rather a test of
# the module's interface.  It tests that the module is
# compatible with the interface of zlib.decompressobj().
#
# The test is run by running this module as a script.
#
# The test is not run automatically by the regrtest.py
# framework, because it requires the zlib module.

import sys
import zlib

def main():
    # Create a decompressor object.
    d = lzma.LZMADecompressor()

    # Feed data to the decompressor object.
    data = d.decompress(b"x\x9cKLJ\x01\x00\x00\x00\x00\x00\x00\x00\x00")
    assert data == b"foo"

    # More data to feed to the decompressor object.
