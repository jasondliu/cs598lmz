import io
# Test io.RawIOBase.readinto()

class TestRawIOBaseReadinto(unittest.TestCase):

    def test_readinto(self):
        class TestRawIO(io.RawIOBase):
            def __init__(self):
                self.readinto_calls = 0
                self.read_calls = 0
                self.closed = 0
            def readinto(self, b):
                self.readinto_calls += 1
                self.read_calls += 1
                return len(b)
            def read(self, n=-1):
                self.read_calls += 1
                return b"x" * n
            def close(self):
                self.closed += 1
        buf = bytearray(10)
        rawio = TestRawIO()
        self.assertEqual(rawio.readinto(buf), 10)
        self.assertEqual(rawio.readinto_calls, 1)
        self.assertEqual(rawio.read_calls, 1)
        self.assertEqual(rawio.closed, 0)
       
