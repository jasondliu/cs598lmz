import lzma
# Test LZMADecompressor.seekable() with a file-like object.
#    >>> decompressor.decompress(data1)
#    >>> decompressor.seekable()
#    False
#    >>> decompressor.decompress(data1, max_length=15)
#    >>> decompressor.seekable()
#    False
#    >>> decompressor.decompress(data2)
#    >>> decompressor.seekable()
#    True
class FileLikeLZMAWrapper(lzma.LZMADecompressor):
    def __init__(self, fileobj):
        super().__init__(format=lzma.FORMAT_XZ)
        self._fileobj = fileobj

    def seekable(self):
        return self._fileobj.seekable()

    def readable(self):
        return self._fileobj.readable()

    def read(self, size=-1):
        return self._fileobj.read(size)

# Unit test:

class TestFileLikeLZMAWrapper(LZMACompressorFileTestsMixin, unittest.
