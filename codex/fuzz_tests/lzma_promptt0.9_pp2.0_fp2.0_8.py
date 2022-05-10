import lzma
# Test LZMADecompressor
assert LZMADecompressor().decompress(
                lzma.compress(b'lzma compression', format=lzma.FORMAT_ALONE, preset=6)
            ) == b'lzma compression'
class BZ2Compressor():
    """
    Modified from BZ2Decompressor by Arun Persaud:
    https://github.com/apersaud/Compression-Examples
    """

    def __init__(self):
        self.compressor = bz2.BZ2Compressor()
        self.unused_data = b''

    def compress(self, data):
        if self.unused_data:
            data = self.unused_data + data

        (compressed, self.unused_data) = self.compressor.compress(data)

        return compressed


class BZ2Decompressor(bz2.BZ2Decompressor):
    """
    Modified from BZ2Decompressor by Arun Persaud:
    https://github.com/apersaud/Compression-Examples

