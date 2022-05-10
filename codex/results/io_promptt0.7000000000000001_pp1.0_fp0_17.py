import io
# Test io.RawIOBase
import io

class IOBase_TestRawIOBase:

    def test_read(self):
        with self.assertRaises(io.UnsupportedOperation):
            self.io.read()

    def test_readall(self):
        with self.assertRaises(io.UnsupportedOperation):
            self.io.readall()

    def test_readinto(self):
        with self.assertRaises(io.UnsupportedOperation):
            self.io.readinto(bytearray(1))

    def test_write(self):
        with self.assertRaises(io.UnsupportedOperation):
            self.io.write(b'')

    @support.cpython_only
    def test_truncate(self):
        # Test that RawIOBase.truncate() implies write access.
        # See also http://bugs.python.org/issue17984.
        self.assertEqual(self.io.truncate(0), 0)
        self.assertRaises(io.UnsupportedOperation, self.io.truncate, 0
