import lzma
# Test LZMADecompressor

with open('data/lzma_data.lzma', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = decompressor.decompress(f.read())
    print(data)

# Test LZMAFile

with lzma.open('data/lzma_data.lzma', 'rb') as f:
    data = f.read()
    print(data)

# Test LZMAFile with a custom filter chain

with lzma.open('data/lzma_data.lzma', 'rb', filters=[
        {"id": lzma.FILTER_LZMA2, "preset": 3 | lzma.PRESET_EXTREME}]) as f:
    data = f.read()
    print(data)

# Test LZMAFile with a custom filter chain and a custom memory limit

with lzma.open('data/lzma_data.lzma', 'rb', filters=[
        {"id": lzma.FILTER
