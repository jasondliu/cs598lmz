import lzma
# Test LZMADecompressor
# https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor

class LZMADecompressor(object):
    def __init__(self):
        self.decompressor = lzma.LZMADecompressor()
        self.unused_data = b''

    def decompress(self, data, max_length=None):
        result = self.decompressor.decompress(data, max_length)
        self.unused_data = data[self.decompressor.unused_data_len:]
        return result

    @property
    def unused_data(self):
        return self.unused_data

    @property
    def eof(self):
        return self.decompressor.eof


class LZMAStreamReader(io.BufferedReader):
    def __init__(self, f, uncompressed_size=None, *args, **kwargs):
        self.uncompressed_size = uncompressed_size
        self.decompressor = L
