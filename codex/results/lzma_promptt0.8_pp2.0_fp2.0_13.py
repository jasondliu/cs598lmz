import lzma
# Test LZMADecompressor
try:
    lzma.LZMADecompressor()
    LZMA_SUPPORTED = True
except AttributeError:
    LZMA_SUPPORTED = False

if sys.version_info[0] == 3:
    class LZMACompressor(Codec):
        """Compression using the LZMA algorithm.

        This requires the `xz` package.
        """
        name = 'lzma'
        description = 'LZMA compression'

        def _compress(self, data):
            d = lzma.LZMACompressor()
            return d.compress(data) + d.flush()
        def _decompress(self, data):
            d = lzma.LZMADecompressor()
            return d.decompress(data)

        def __repr__(self):
            return "{0}()".format(self.__class__.__name__)

    if LZMA_SUPPORTED:
        bz2 = LZMACompressor()
else:
    class LZ
