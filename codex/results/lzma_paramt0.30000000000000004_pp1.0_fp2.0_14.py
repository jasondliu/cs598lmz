from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Outputs: b'hello'

# The LZMA file format is a container format. The first byte is the "properties byte" that encodes the LZMA compression properties. The next eight bytes are the uncompressed size of the file, encoded as a 64-bit little-endian integer. The rest of the file is the LZMA-compressed data stream.

# The lzma module provides support for compressing and decompressing data using the LZMA compression algorithm. It supports the LZMA2 format used by the XZ Utils package, and can also read the legacy LZMA format used by older versions of XZ Utils.

# The LZMAFile class provides a file-like interface for reading and writing LZMA-compressed files.

# The LZMAFile class supports the context management protocol.
