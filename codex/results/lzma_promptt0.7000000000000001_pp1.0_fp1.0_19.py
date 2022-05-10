import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor(
        filters=[
            {"id": lzma.FILTER_LZMA2,
             "preset": 9 | lzma.PRESET_EXTREME},
        ])

decompressor = lzma.LZMADecompressor()

with open('test-file.txt', 'rb') as testfile:
    source_data = testfile.read(100)
    compressed = compressor.compress(source_data)
    compressed += compressor.flush()

# data = decompressor.decompress(compressed)
# print('The first 100 bytes of the decompressed data:')
# print(data[:100])

data = b''
decompressor = lzma.LZMADecompressor()
for chunk in compressed:
    data += decompressor.decompress(chunk)

print(data[:100])

# Test LZMAFile

with lzma.open('test-file.txt') as f:
    data1 = f.read(16)
