import bz2
# Test BZ2Decompressor.max_length
class TestMaxLength:
    def __init__(self, test_name, compressor, blocksize=100000, max_length=10):
        self.test_name = test_name
        self.compressor = compressor
        self.blocksize = blocksize
        self.max_length = max_length

    def __call__(self):
        decompressor = bz2.BZ2Decompressor(max_length=self.max_length)
        data = b'A' * self.blocksize
        compressed_data = self.compressor.compress(data)
        try:
            decompressor.decompress(compressed_data)
        except Exception as e:
            if (isinstance(e, EOFError) and
                "MAX_LENGTH" in str(e)):
                return
            raise
        raise Exception("didn't raise with max length exceeded")


class TestMaxLengthBlocksize0(TestMaxLength):
    def __init__(self, test_name, compressor, max_length=10):
        super().__init__(test
