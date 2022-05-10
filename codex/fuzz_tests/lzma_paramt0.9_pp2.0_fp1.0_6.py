from lzma import LZMADecompressor
LZMADecompressor.__module__ = None
try:
    import bz2
    BZ2Decompressor = bz2.BZ2Decompressor
except (ImportError, AttributeError):
    from bz2 import BZ2Decompressor

MAX_VOLUME_SIZE = 1024 * 1024 * 1024


class DeflateDecompressor(object):
    """Decompressor for Deflate stream in Zipfile, gzip and zlib.
    """

    def __init__(self, wbits, method):
        self.method = method
        self.decompressobj = zlib.decompressobj(-wbits)

    def decompress(self, data):
        if self.method == 8:
            data = self.decompressobj.decompress(data)
            data += self.decompressobj.flush()
            return data
        else:
            logger.error("unknown compression method {}".format(self.method))
            return b''


def ReadNetstrings(fd):
    """Read a netstring-encoded string."""
    size = 0
    while True
