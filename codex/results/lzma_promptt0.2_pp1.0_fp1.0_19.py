import lzma
# Test LZMADecompressor

with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = f.read(10)
    while data:
        print(decompressor.decompress(data))
        data = f.read(10)

# Test LZMAFile

with lzma.open('test.xz') as f:
    print(f.read())

# Test LZMAFile with filters

with lzma.open('test.xz', format=lzma.FORMAT_RAW, filters=[
        {"id": lzma.FILTER_LZMA2, "preset": 3 | lzma.PRESET_EXTREME}]) as f:
    print(f.read())

# Test LZMAFile with mode

with lzma.open('test.xz', mode='wt') as f:
    f.write('test')

with lzma.open('test.xz', mode='rt') as f:
    print(f.read())
