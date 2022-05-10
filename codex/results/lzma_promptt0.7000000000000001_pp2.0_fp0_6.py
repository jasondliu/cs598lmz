import lzma
# Test LZMADecompressor
lzma_decompressor = lzma.LZMADecompressor()
data = lzma_decompressor.decompress(compressed_data)
print(len(data))
print(data)

print()

# Test LZMACompressor
lzma_compressor = lzma.LZMACompressor()
compressed_data = lzma_compressor.compress(b'data to compress')
compressed_data += lzma_compressor.flush()
print(compressed_data)
print(lzma_compressor.unused_data)

# Test LZMAFile
with lzma.open('./bz2_compress.py.xz', 'rb') as lzma_file:
    file_content = lzma_file.read()
    print(file_content)

# Test LZMAError
try:
    lzma.decompress(b'This is not compressed with LZMA')
except lzma.LZMAError as err:
    print('Error
