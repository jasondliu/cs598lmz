from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output:
# b'hello'

# The LZMA library can also be used to create LZMA-compressed files or data streams:

from lzma import LZMAFile
with LZMAFile('lzma_compressed.xz', 'w') as f:
    f.write(b'hello world!')

# The LZMAFile class is a file-like object that reads and writes LZMA-compressed data.
# It can be used as a drop-in replacement for a GzipFile or BZ2File object in many cases.

# The LZMAFile class supports the context management protocol.
# When used in a with statement, the file is automatically closed.

# The LZMAFile class also supports the iterator protocol.
# Each iteration returns a chunk
