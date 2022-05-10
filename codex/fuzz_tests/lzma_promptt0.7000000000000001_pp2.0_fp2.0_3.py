import lzma
# Test LZMADecompressor class

# Make a dummy file with a magic number at the beginning and a known checksum
# at the end.

with open('test.xz', 'w+b') as f:
    f.write(b'\xfd7zXZ\x00')
    f.write(b'\x00' * 5)
    f.write(lzma.CHECK_NONE)
    f.write(lzma.FILTER_LZMA1)
    f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00')
    f.write(b'\x00\x00\x20')
    f.write(b'\x00' * 6)
    f.write(b'\x01')
    f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00')
    f.write(b'\x00\x00\x00\x00\x00\x00\x00\x00\x
