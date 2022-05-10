import lzma
# Test LZMADecompressor
with open('data/file.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = decompressor.decompress(f.read())
    print(data)

# Test LZMAFile
with lzma.open('data/file.xz', 'rb') as f:
    print(f.read())

# Test LZMAFile for writing
with lzma.open('data/file.xz', 'wb') as f:
    f.write(b'Hello, world!')

# Test LZMAFile for writing with a preset
with lzma.open('data/file.xz', 'wb', preset=9 | lzma.PRESET_EXTREME) as f:
    f.write(b'Hello, world!')

# Test LZMAFile for writing with filters
filters = [
    {"id": lzma.FILTER_LZMA2, "preset": 9 | lzma.PRESET_EXTREME},
    {"id": lz
