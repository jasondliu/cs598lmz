import lzma
# Test LZMADecompressor

# This is a simple test of the LZMADecompressor class.
# It is not intended to be complete.

# The test data is a file containing the string "foo
# bar baz" repeated many times.  The file is compressed
# with xz at various compression levels and with various
# settings.

import lzma
import os
import sys

def test(filename):
    with open(filename, "rb") as f:
        decomp = lzma.LZMADecompressor()
        data = f.read()
        assert decomp.decompress(data) == b"foo bar baz" * 1000
        assert decomp.unused_data == b""
        assert decomp.eof
        assert not decomp.is_finished

def test_stream(filename):
    with open(filename, "rb") as f:
        decomp = lzma.LZMADecompressor()
        data = f.read()
        assert decomp.decompress(data[:100]) == b""
        assert decomp.decompress(data[100:])
