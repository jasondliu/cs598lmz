import lzma
# Test LZMADecompressor for decompression in seekable mode

# Trivial compressed data
compressed = b"\x17\x16\x15\x14\x13\x12\x11\x10\xff\xce\x00\x00\xfb\x00\x0b\x00"

c = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE,
                          check=lzma.CHECK_NONE,
                         )
# Fill LZMACompressor with inital bytes
c.decompress(b'\x00\x00\xff\xff')

# Decompress initial bytes
decompress = c.decompress(compressed)

print(decompress)
c.decompress(b'\x55\x55')
c.decompress()
