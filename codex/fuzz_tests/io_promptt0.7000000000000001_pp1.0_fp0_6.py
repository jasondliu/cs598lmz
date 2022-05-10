import io
# Test io.RawIOBase with an object with a readable buffer interface
# (like BytesIO, or something that supports the buffer protocol).

import io
import _io
import pickle
import sys

try:
    import _testbuffer
except ImportError:
    _testbuffer = None


# A mixin for testing RawIOBase with an object with a readable buffer
# interface (e.g. BytesIO, or something that supports the buffer
# protocol).
class BufferIOMixin:

    rawio_class = None
    has_readall = False

    def new_io(self, initial_bytes):
        # Make a new RawIO object for testing.
        if initial_bytes is None:
            return self.rawio_class(self.BUFFER())
        else:
            return self.rawio_class(self.BUFFER(initial_bytes))

    def test_read(self):
        # Test RawIOBase.read()
        io = self.new_io(b'abcdef')
        self.assertEqual(io.read(2), b'ab')
        self.assertE
