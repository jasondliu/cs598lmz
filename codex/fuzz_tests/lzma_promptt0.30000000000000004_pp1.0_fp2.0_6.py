import lzma
# Test LZMADecompressor

with open('test.xz', 'rb') as f:
    d = lzma.LZMADecompressor()
    data = f.read()
    print(d.decompress(data))

# Test LZMAFile

with lzma.open('test.xz', 'rb') as f:
    print(f.read())

# Test LZMAFile with filters

with lzma.open('test.xz', 'rb', filters=[{'id': lzma.FILTER_LZMA2, 'preset': 9 | lzma.PRESET_EXTREME}]) as f:
    print(f.read())

# Test LZMAFile with a custom filter

with lzma.open('test.xz', 'rb', filters=[
        {'id': lzma.FILTER_LZMA2, 'preset': 9 | lzma.PRESET_EXTREME},
        {'id': lzma.FILTER_DELTA, 'dist': 2},
    ]) as f:
