import lzma
# Test LZMADecompressor
d = lzma.LZMADecompressor()
d.decompress(b"\x00" * 5 + b"\x01\x20\x00\x00\x00\x00\x00\x08\x00\x03\x00\x04\x00\x05\x00\x00")

# Test LZMACompressor
c = lzma.LZMACompressor()
c.compress(b"foo")
c.flush()
"""

# lzma.compress(data, format=FORMAT_XZ, check=CHECK_CRC64, preset=None, filters=None)
# lzma.decompress(data, format=FORMAT_AUTO, memlimit=None, filters=None)

print()
