import lzma
# Test LZMADecompressor
with open('/usr/share/man/man1/Python.1.gz', 'rb') as f:
    print(lzma.decompress(f.read()))
    
# Test LZMACompressor/LZMADecompressor
s = lzma.LZMACompressor().compress(b"foo")
print(s)
print(lzma.LZMADecompressor().decompress(s))

# test other constants
print(lzma.FORMAT_AUTO)
print(lzma.FORMAT_XZ)
print(lzma.PRESET_DEFAULT)
print(lzma.CHECK_CRC32)
print(lzma.CHECK_CRC64)
print(lzma.CHECK_SHA256)

# Test LZMAFile
with open('/usr/share/man/man1/Python.1.xz', 'rb') as f:
    with lzma.LZMAFile(f) as xz:
        print(xz.read())

# Test
