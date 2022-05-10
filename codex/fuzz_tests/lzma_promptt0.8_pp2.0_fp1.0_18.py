import lzma
# Test LZMADecompressor for bugs
compressor = lzma.LZMADecompressor()
compressor.decompress(b'\x00' * 8)
compressor.decompress(b'\x00' * 8)
# Test LZMAFile for bugs
with open('Tests/files/xz-empty.xz', 'rb') as f:
    lzma.LZMAFile(f).read()
# Test LZMAFile.seek()
with open('Tests/files/xz-empty.xz', 'rb') as f:
    f = lzma.LZMAFile(f)
    f.read()
    pos = f.tell()
    f.seek(pos)
    f.read()
    f.seek(pos)
    f.seek(pos, 0)
# Test LZMAFile.seek(0, 1)
with open('Tests/files/xz-empty.xz', 'rb') as f:
    f = lzma.LZMAFile(f)
    f.seek(0, 1)

