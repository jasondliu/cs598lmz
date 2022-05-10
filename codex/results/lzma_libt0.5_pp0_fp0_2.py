import lzma
lzma_codec = codecs.lookup("lzma")
lzma_codec.encode = lzma.compress
lzma_codec.decode = lzma.decompress


class LZMACompressor(Compressor):
    """Compressor that uses LZMA to compress the data.

    The recommended settings for this compressor are:

    * :attr:`~Compressor.compresslevel` = 9
    * :attr:`~Compressor.shuffle` = 1
    """

    def __init__(self, compresslevel=9, shuffle=1):
        super().__init__(compresslevel, shuffle)

    def _get_codec(self):
        return lzma_codec


class LZMADecompressor(Decompressor):
    """Decompressor that uses LZMA to decompress the data."""

    def _get_codec(self):
        return lzma_codec


class BZ2Compressor(Compressor):
    """Compressor that uses BZ2 to compress the data.
