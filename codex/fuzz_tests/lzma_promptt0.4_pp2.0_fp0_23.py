import lzma
# Test LZMADecompressor

with open('lzma_compressed.bin', 'rb') as f:
    data = f.read()

decompressor = lzma.LZMADecompressor()
result = decompressor.decompress(data)

print(result)

with open('lzma_decompressed.bin', 'wb') as f:
    f.write(result)

print(len(result))

# Test LZMAFile

with lzma.open('lzma_compressed.bin', 'rb') as f:
    result = f.read()

print(result)

with open('lzma_decompressed.bin', 'wb') as f:
    f.write(result)

print(len(result))

# Test LZMAFile with filters

with lzma.open('lzma_compressed.bin', 'rb', filters=[
        {'id': lzma.FILTER_LZMA1, 'preset': 9 | lzma.PRESET_EXTREME}]) as f:
