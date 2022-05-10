import lzma
# Test LZMADecompressor to see if it supports the CHECK_CRC32 option.
try:
    lzma.LZMADecompressor(lzma.CHECK_CRC32)
    class _LZMAFile(object):
        def open(self, filename, mode="rb"):
            return lzma.LZMAFile(filename, mode)
except TypeError:
    class _LZMAFile(object):
        def open(self, filename, mode="rb"):
            return lzma.LZMAFile(filename, mode, format=lzma.FORMAT_ALONE)
        def decompress(self, data):
            return lzma.decompress(data)

class BZ2File(_BZ2File):
    def decompress(self, data):
        return bz2.decompress(data)

class GzipFile(_GzipFile):
    def decompress(self, data):
        return zlib.decompress(data, zlib.MAX_WBITS | 16)
