import io
# Test io.RawIOBase

import io
import errno

class TestRawIOBase:

    def test_readline(self):
        # Readline returns bytes from the stream
        rawio = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, rawio.readline)

    def test_readlines(self):
        # Readlines returns bytes from the stream
        rawio = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, rawio.readlines)

    def test_writelines(self):
        # Writelines accepts an iterable of bytes
        rawio = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, rawio.writelines, [])

    def test_seekable(self):
        # A RawIOBase is not seekable by default
        rawio = io.RawIOBase()
        self.assertFalse(rawio.seekable())

    def test_readable(self):
        # A RawIOBase is not readable by default
        rawio = io.RawIOBase()
