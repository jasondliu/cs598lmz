import io
# Test io.RawIOBase()
class RawIOBaseTest(unittest.TestCase):
    def test_read(self):
        # Test that an exception is raised when the base implementation
        # is used.
        self.assertRaises(IOError, io.RawIOBase().read)

    def test_readinto(self):
        # Test that an exception is raised when the base implementation
        # is used.
        self.assertRaises(IOError, io.RawIOBase().readinto, bytearray())

    def test_readline(self):
        # Test that an exception is raised when the base implementation
        # is used.
        self.assertRaises(IOError, io.RawIOBase().readline)

    def test_readinto_negative(self):
        # Test that a ValueError is raised if the length of b is less than 0.
        self.assertRaises(ValueError, io.RawIOBase().readinto, bytearray(), -1)

    def test_readall(self):
        # Test that an exception is raised when the base implementation
        # is used.

