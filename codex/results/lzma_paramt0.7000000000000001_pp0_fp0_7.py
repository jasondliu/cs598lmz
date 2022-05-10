from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

# LZMA-compressed data can be appended to other data
lzma_data = lzma.compress(b'ABC') + lzma.compress(b'DEF')

decompressor = LZMADecompressor()

decompressor.decompress(lzma_data)  # b'ABC'
decompressor.decompress(b'GHI')     # b'DEFGHI'

"""

"""
# try to make a class of LZMADecompressor()

# The following code is from https://github.com/python/cpython/blob/master/Lib/lzma.py

class LZMADecompressor:

    def __init__(self, format=FORMAT_AUTO, memlimit=None, filters=None):
        self._buffer = BytesIO()
        self._eof = False
        self._unused_data = b""
        if format == FORMAT_AUTO:
            format = FORMAT_XZ

