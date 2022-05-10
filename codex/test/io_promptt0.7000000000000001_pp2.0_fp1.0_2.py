import io
# Test io.RawIOBase.read()

# This test checks that io.RawIOBase.read() returns an empty bytes
# object (not None) when the stream is at EOF, and that it returns
# None when the maximum length is zero.

import _io

