import lzma
# Test LZMADecompressor and LZMACompressor

class Compress:
    def __init__(self, inbytes, level=9):
        self.inbytes = inbytes
        self.cbytes = self.compress_lzma(level)
    def compress_lzma(self, level):
        compressor = lzma.LZMACompressor(level)
        return compressor.compress(self.inbytes) + compressor.flush()
    def get_cbytes(self):
        return self.cbytes
    def get_len_cbytes(self):
        return len(self.cbytes)
    def get_len_inbytes(self):
        return len(self.inbytes)

class Decompress:
    def __init__(self, cbytes, level=9):
        self.cbytes = cbytes
        self.inbytes = self.decompress_lzma(level)
    def decompress_lzma(self, level):
        decompressor = lzma.LZMADecompressor(level)
        return decompressor.decompress
