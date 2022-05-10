import lzma
lzma.LZMA_PRESET = 9

class LZMACompressor(object):
    def __init__(self):
        self.compressor = lzma.LZMACompressor()
    def compress(self, data):
        return self.compressor.compress(data)
    def flush(self):
        return self.compressor.flush()

class LZMADecompressor(object):
    def __init__(self):
        self.decompressor = lzma.LZMADecompressor()
    def decompress(self, data):
        return self.decompressor.decompress(data)
    def flush(self):
        return self.decompressor.flush()

class LZMACompression(Compression):
    def __init__(self):
        super().__init__()
        self.compressor = LZMACompressor()
        self.decompressor = LZMADecompressor()
        self.name = "LZMA"
        self.extension = "lzma"
        self
