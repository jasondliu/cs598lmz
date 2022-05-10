import io
# Test io.RawIOBase
class io_RawIOBase(unittest.TestCase):
    def test_readinto(self):
        self.assertEquals(io.RawIOBase.readinto.im_func(
                io.BytesIO('a'), 'b'), 1)
        self.assertEquals(io.RawIOBase.readinto.im_func(
                io.BytesIO('abc'), 'd'), 3)


class BufferSizeRecorder(io.RawIOBase):
    def __init__(self):
        self.total_size = 0
        self.total_chunks = 0

    def write(self, b):
        self.total_size += len(b)
        self.total_chunks += 1


class GzipBufferTests(unittest.TestCase):
    def setUp(self):
        self.size_recorder = BufferSizeRecorder()

    # The following two tests are a copy of the tests in
    # Lib/test/test_gzip.py, but we want them to run without having
    # the full test suite, so we keep them here
