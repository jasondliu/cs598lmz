import io
# Test io.RawIOBase.readinto()
import _testcapi

class TestRawIO(unittest.TestCase):

    def test_readinto(self):
        # Test RawIO.readinto()
        a = array.array('b', [0, 1, 2, 3])
        b = array.array('b', [0]*4)
        class ReadIntoWrapper(io.RawIOBase):
            def readinto(self, b):
                self.readinto_called = True
                return super().readinto(b)
        # Test readinto() with a writable array
        with ReadIntoWrapper() as s:
            s.write(a.tobytes())
            s.seek(0)
            self.assertEquals(s.readinto(b), len(a))
            self.assertEquals(a, b)
            self.assertEquals(s.readinto(b), 0)
            self.assertEquals(s.readinto(b), 0)
            self.assertTrue(s.readinto_called)

    def test_readall(
