import io
# Test io.RawIOBase.readinto()

class TestRawIOBaseReadinto(unittest.TestCase):

    def test_readinto(self):
        rawio = io.RawIOBase()
        self.assertRaises(io.UnsupportedOperation, rawio.readinto, b"")

class TestRawIOBaseReadintoBuffer(unittest.TestCase):

    def test_readinto_buffer(self):
        rawio = io.RawIOBase()
        b = bytearray(4)
        self.assertRaises(TypeError, rawio.readinto, b)

    def test_readinto_non_contiguous_buffer(self):
        rawio = io.RawIOBase()
        a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
        b = memoryview(a)[2:6]
        self.assertRaises(TypeError, rawio.readinto, b)

# Test the file object's ability to deal with its own buffers

test_data = b"test data"

class TestFileContext
