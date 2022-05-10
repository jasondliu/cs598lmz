import io
# Test io.RawIOBase.readinto

class BaseTestRawIO(unittest.TestCase):

    def test_readinto_negative_arg(self):
        # Issue #20202: readinto() should raise OSError for negative arguments
        rawio = io.RawIOBase()
        self.assertRaises(OSError, rawio.readinto, -1)


class BaseTestRawBufferedIO(unittest.TestCase):

    def test_readinto_negative_arg(self):
        # Issue #20202: readinto() should raise OSError for negative arguments
        rawio = io.BufferedIOBase()
        self.assertRaises(OSError, rawio.readinto, -1)


class BaseTestBufferedIO(unittest.TestCase):

    def test_readinto_negative_arg(self):
        # Issue #20202: readinto() should raise OSError for negative arguments
        rawio = io.BufferedIOBase()
        self.assertRaises(OSError, rawio.readinto, -1)


class BaseTestTextIO
