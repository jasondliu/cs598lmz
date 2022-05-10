from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')
#b'Hello World'
print(LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00'))

# The lzma module also provides a LZMADecompressor class for decompressing data incrementally.
# This class is not compatible with the LZMAFile class, but it does have the same interface as the zlib.decompressobj() class.
# For example:

from lzma import LZMADecompressor
decompressor = LZMADecompressor()
decompressor.decompress(b
