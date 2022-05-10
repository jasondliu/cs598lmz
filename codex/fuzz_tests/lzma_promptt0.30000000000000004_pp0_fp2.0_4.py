import lzma
# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()

with open('test.xz', 'rb') as f:
    file_content = f.read()

decompressed_data = decompressor.decompress(file_content)

print(decompressed_data)

# Test LZMAFile

with lzma.open('test.xz', 'rb') as f:
    file_content = f.read()

print(file_content)

# Test LZMAFile with filters

filters = [
    {"id": lzma.FILTER_LZMA2, "preset": 3 | lzma.PRESET_EXTREME},
    {"id": lzma.FILTER_DELTA, "dist": 5},
]

with lzma.open('test.xz', 'rb', filters=filters) as f:
    file_content = f.read()

print(file_content)

# Test LZMAFile with multiple filters

filters = [
    {"id
