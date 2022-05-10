import io
# Test io.RawIOBase.readall()

class TestRawIOBase(unittest.TestCase):
    def setUp(self):
        self.r = io.RawIOBase()
        self.r.read = lambda n: b'x' * n

    def test_readall(self):
        self.assertEqual(self.r.readall(), b'x' * io.DEFAULT_BUFFER_SIZE)

    def test_readall_custom(self):
        self.assertEqual(self.r.readall(5), b'xxxxx')


if __name__ == "__main__":
    unittest.main()
