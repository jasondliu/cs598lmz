import io
# Test io.RawIOBase.readinto()

class TestRawIOBaseReadinto(unittest.TestCase):

    def test_readinto_with_no_arguments(self):
        # Test that readinto() raises a TypeError when called with no
        # arguments.
        class MyRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                self.readinto_called_with = b
                return 42
        rawio = MyRawIO()
        self.assertRaises(TypeError, rawio.readinto)

    def test_readinto_with_too_many_arguments(self):
        # Test that readinto() raises a TypeError when called with too
        # many arguments.
        class MyRawIO(io.RawIOBase):
            def readable(self):
                return True
            def readinto(self, b):
                self.readinto_called_with = b
                return 42
        rawio = MyRawIO()
        self.assertRaises(TypeError, rawio.readinto, b"",
