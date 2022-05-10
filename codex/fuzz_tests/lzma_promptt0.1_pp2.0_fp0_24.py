import lzma
# Test LZMADecompressor

with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = f.read(10)
    while data:
        print(decompressor.decompress(data))
        data = f.read(10)

# Test LZMAFile

with lzma.open('test.xz', 'rb') as f:
    print(f.read())

# Test LZMAFile with filters

with lzma.open('test.xz', 'rb', filters=[{"id": lzma.FILTER_LZMA2, "preset": 3}]) as f:
    print(f.read())

# Test LZMAFile with a custom preset

with lzma.open('test.xz', 'rb', preset=9 | lzma.PRESET_EXTREME) as f:
    print(f.read())

# Test LZMAFile with a custom filters

with lzma.open('test.xz', 'rb', filters=[
