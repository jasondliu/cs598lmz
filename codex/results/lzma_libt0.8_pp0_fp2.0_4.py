import lzma
lzma_compressor = lzma.LZMACompressor(preset=6, check=lzma.CHECK_CRC64)
lzma_decompressor = lzma.LZMADecompressor(check=lzma.CHECK_CRC64)
 
class LzmaCompressor(Compressor):
    def __init__(self, opts):
        super(LzmaCompressor, self).__init__(opts)

    def compress(self, data):
        return lzma_compressor.compress(data) + lzma_compressor.flush()

    def decompress(self, data):
        return lzma_decompressor.decompress(data)

class LzmaPlugin(Plugin):
    def __init__(self, opts):
        super(LzmaPlugin, self).__init__(opts)
        self.opts = opts

    def get_compressor(self):
        return LzmaCompressor(self.opts)

plugin_class = LzmaPlugin
