from lzma import LZMADecompressor
LZMADecompressor.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')

# uncompressed data is b'12345abcde'

# The decompressor object also provides some other useful attributes and methods:

>>> decompressor.unused_data
b''
>>> decompressor.eof
True
>>> decompressor.decompress(b'more data')
b''
>>> decompressor.unused_data
b'more data'
>>> decompressor.eof
False

# The unused_data attribute contains any data that was passed to decompress() but not
# consumed by the decompressor yet. The eof attribute is True when the end of the compressed
# data stream has been reached.

# The decompressor can be used as a context manager, in which case it automatically
# calls flush() at the end of the block to finish the decompression.

>>> with LZMAD
