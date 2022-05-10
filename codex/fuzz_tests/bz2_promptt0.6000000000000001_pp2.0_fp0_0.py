import bz2
# Test BZ2Decompressor
try:
    import bz2
    bz2.decompress(b"BZ")
except:
    pass
else:
    class BZ2Decompressor(Decompressor):
        def __init__(self):
            self.decomp = bz2.BZ2Decompressor()

        def decompress(self, data):
            return self.decomp.decompress(data)

        def flush(self):
            return self.decomp.flush()

    _decompressors["bz2"] = BZ2Decompressor

# Test LZMADecompressor
try:
    import lzma
    lzma.LZMADecompressor().decompress(b"")
except:
    pass
else:
    class LZMADecompressor(Decompressor):
        def __init__(self):
            self.decomp = lzma.LZMADecompressor()

        def decompress(self, data):
            return self.decomp.decompress(data)

        def flush(
