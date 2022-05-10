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
