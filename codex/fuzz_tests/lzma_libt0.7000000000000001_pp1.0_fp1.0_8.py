import lzma
lzma.LZMA_VERSION

class LzmaDecompressor(Decompressor):
    def __init__(self):
        Decompressor.__init__(self)
        self._decomp = lzma.LZMADecompressor()

    def decompress(self, data):
        ret = self._decomp.decompress(data)
        if not ret:
            raise EOFError
        return ret
