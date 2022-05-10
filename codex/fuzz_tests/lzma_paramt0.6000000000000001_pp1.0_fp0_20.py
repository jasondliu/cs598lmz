from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')
# b'Hello'

# The LZMA-compressed data must include a valid end-of-stream marker.
# Otherwise, the decompressor will raise an EOFError exception.
LZMADecompressor().decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00')
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "/usr/local/lib/python3.2/lzma.py", line 195, in decompress
#    return self.decompressobj.decompress
