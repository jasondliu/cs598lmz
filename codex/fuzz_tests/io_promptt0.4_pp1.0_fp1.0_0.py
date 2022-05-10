import io
# Test io.RawIOBase

import io
import _io

# This test checks the RawIOBase implementation using a raw file object.
# It is not meant to be complete.

# Open a file for reading and writing.
f = open(io.__file__, 'r+b')
try:
    # Create a raw file object.
    raw = _io.FileIO(f.fileno(), closefd=False)
    try:
        # Test read()
        assert raw.read(5) == b'# -*-'
        # Test write()
        raw.write(b'hi there')
        # Test seek()
        raw.seek(0, 0)
        assert raw.read(5) == b'# -*-'
        # Test tell()
        assert raw.tell() == 5
        # Test seek() with whence=1
        raw.seek(-5, 1)
        assert raw.read(5) == b'# -*-'
        # Test seek() with whence=2
        raw.seek(-5, 2)
        assert raw.read(5) == b'# -*
