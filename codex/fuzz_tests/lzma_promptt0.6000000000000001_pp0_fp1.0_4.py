import lzma
# Test LZMADecompressor
with lzma.open('text.xz') as f:
    file_content = f.read()
    print(file_content)

print(file_content == original_data)

# Test LZMACompressor
compressor = lzma.LZMACompressor()

with open('text.xz', 'wb') as f:
    f.write(compressor.compress(original_data))
    f.write(compressor.flush())

with lzma.open('text.xz') as f:
    file_content = f.read()

print(file_content == original_data)

os.remove('text.xz')

# Test LZMADecompressor.get_decompress_size
with lzma.open('text.xz') as f:
    print(f.get_decompress_size())

# Test LZMADecompressor.flush
compressor = lzma.LZMACompressor()

with open('text.xz', 'wb') as f:
   
