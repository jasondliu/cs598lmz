import io
# Test io.RawIOBase
class testRawIOBase(unittest.TestCase):

    def test_read(self):
        # io.RawIOBase.read()
        self.assertRaises(TypeError, io.RawIOBase().read)

    def test_readinto(self):
        # io.RawIOBase.readinto()
        self.assertRaises(TypeError, io.RawIOBase().readinto)

    def test_write(self):
        # io.RawIOBase.write()
        self.assertRaises(TypeError, io.RawIOBase().write)

    @support.refcount_test
    def test_del(self):
        b = io.BufferedReader(io.BytesIO())
        weak = weakref.ref(b)
        del b
        self.assertIs(weak(), None)

    def _check_readable_writable(self, raw, readable, writable):
        self.assertEqual(raw.readable(), readable)
        self.assertEqual(raw.writable(), writable)
        self.assertEqual(raw.seekable
