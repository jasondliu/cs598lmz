import io
# Test io.RawIOBase

import _io

class TestRawIOBase:

    def test_read(self):
        # Read at most 0 bytes.
        rawio = _io.RawIOBase()
        self.assertRaises(TypeError, rawio.read)
        self.assertRaises(TypeError, rawio.read, None)
        self.assertRaises(TypeError, rawio.read, 'foo')
        self.assertRaises(TypeError, rawio.read, b'foo')
        self.assertRaises(TypeError, rawio.read, bytearray(b'foo'))
        self.assertRaises(TypeError, rawio.read, memoryview(b'foo'))
        self.assertRaises(TypeError, rawio.read, array.array('b', b'foo'))
        self.assertRaises(TypeError, rawio.read, 0.0)
        self.assertRaises(TypeError, rawio.read, 0j)
        self.assertRaises(TypeError, rawio.read, object())
