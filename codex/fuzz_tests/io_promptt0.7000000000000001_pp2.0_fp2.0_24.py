import io
# Test io.RawIOBase
class RawIOBaseTests(unittest.TestCase):

    def test_close_flushes(self):
        class TestRawIO(io.RawIOBase):
            closed = 0
            def close(self):
                self.closed += 1
        rawio = TestRawIO()
        self.assertFalse(rawio.closed)
        rawio.close()
        self.assertTrue(rawio.closed)

    def test_detach(self):
        # The C implementation always returns None, and the Python
        # implementation can't do anything else, so we're happy just
        # to verify that the method exists.
        io.RawIOBase().detach()

    def test_read(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().read)

    def test_readinto(self):
        self.assertRaises(io.UnsupportedOperation, io.RawIOBase().readinto,
                          bytearray())

    def test_readall(self):
        self.assertRaises(io.UnsupportedOperation, io
