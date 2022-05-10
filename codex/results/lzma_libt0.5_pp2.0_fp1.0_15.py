import lzma
lzma.LZMAError

class LZMACompressor(object):
    def __init__(self, level=6):
        self.level = level
        self.compressor = lzma.LZMACompressor(preset=self.level)

    def compress(self, data):
        return self.compressor.compress(data)

    def flush(self):
        return self.compressor.flush()

class LZMADecompressor(object):
    def __init__(self):
        self.decompressor = lzma.LZMADecompressor()

    def decompress(self, data, max_length=0):
        return self.decompressor.decompress(data, max_length)

try:
    import lz4.frame
    lz4.frame.LZ4FrameError
except (ImportError, AttributeError):
    lz4 = None

if lz4:
    class LZ4Compressor(object):
        def __init__(self, level=1):
            self.level
