import lzma
lzma.open

from io import BytesIO
from lzma import open as lzma_open, LZMAFile

from .base import BaseCompressor


class LZMACompressor(BaseCompressor):
    """
    Compress data using LZMA
    """

    def __init__(self, options=None):
        """
        Init the compressor
        """
        super().__init__(options=options)
        if options is None:
            self.options = dict(level=9)
        else:
            self.options = options

    def compress(self, data):
        """
        Compress data
        """
        if not isinstance(data, bytes):
            data = data.encode("utf-8")
        return LZMAFile(BytesIO(data), "w", **self.options).read()

    def decompress(self, data):
        """
        Decompress data
        """
        return lzma_open(BytesIO(data)).read().decode("utf-8")
