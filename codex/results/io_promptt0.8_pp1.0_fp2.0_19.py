import io
# Test io.RawIOBase
class RawIOBaseTests(unittest.TestCase):

    def test_readinto(self):
        class MockRawIO(io.RawIOBase):
            def __init__(self, reads):
                self._reads = iter(reads)

            def readinto(self, b):
                r = next(self._reads)
                if r:
                    b[:len(r)] = r
                return len(r)

        # This is a very partial test to ensure that readinto()
        # behaves as expected.
        b = bytearray(20)
        mock = MockRawIO([b'abc', b'', b'def', b'ghij'])
        self.assertEqual(mock.readinto(b), 3)
        self.assertEqual(b[:3], b'abc')
        self.assertEqual(mock.readinto(b), 0)
        self.assertEqual(mock.readinto(b), 3)
        self.assertEqual(b[:3], b'def')
        self.assertEqual
