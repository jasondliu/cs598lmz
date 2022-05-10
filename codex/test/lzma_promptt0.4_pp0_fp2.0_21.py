import lzma
# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()

with open('test.xz', 'rb') as f:
    data = f.read()
    decompressed = decompressor.decompress(data)
    print(decompressed.decode('utf-8'))

# Test LZMAFile

with lzma.open('test.xz', 'rb') as f:
    data = f.read()
    print(data.decode('utf-8'))

# Test LZMAFile with filters

filters = [
    {"id": lzma.FILTER_LZMA1, "preset": 9 | lzma.PRESET_EXTREME},
    {"id": lzma.FILTER_DELTA, "dist": 5},
]

