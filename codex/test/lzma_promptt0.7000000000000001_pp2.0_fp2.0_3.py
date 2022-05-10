import lzma
# Test LZMADecompressor class

# Make a dummy file with a magic number at the beginning and a known checksum
# at the end.

with open('test.xz', 'w+b') as f:
    f.write(b'\xfd7zXZ\x00')
    f.write(b'\x00' * 5)
