import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

# Issue #23359: test that the weakref callback is called when the
# BufferedReader is finalized.
class FinalizeTest(unittest.TestCase):
    def setUp(self):
        self.callback_called = False
        self.callback_called_with = None

    def callback(self, obj):
        self.callback_called = True
        self.callback_called_with = obj

    def test_finalize(self):
        f = io.BufferedReader(File())
        f.read(1)
        wr = weakref.ref(f, self.callback)
        del f
        self.assertTrue(self.callback_called)
        self.assertIsNone(self.callback_called_with)

class TestBufferedReader(unittest.TestCase):
    def test_constructor(self):
        rawio = io.BytesIO(b"ABC")
        bufio = io.BufferedReader(rawio)
        self.assertEqual(bufio.raw.read(), b"ABC")

    def test_read(self):
