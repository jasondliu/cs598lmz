import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    def test_readinto(self):
        # RawIOBase.readinto()
        class TestRawIO(io.RawIOBase):
            def __init__(self):
                self.read_stack = [b"abc", b"def", b"ghi", b"jkl"]
            def readinto(self, b):
                data = self.read_stack.pop(0)
                n = len(data)
                b[:n] = data
                return n
            def readable(self):
                return True
        buf = bytearray(4)
        f = TestRawIO()
        n = f.readinto(buf)
        self.assertEqual(n, 3)
        self.assertEqual(buf, b"abc")
        n = f.readinto(buf)
        self.assertEqual(n, 3)
        self.assertEqual(buf, b"def")
        n = f.readinto(buf)
        self.assertEqual(n, 3)
