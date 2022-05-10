import lzma
# Test LZMADecompressor
with lzma.open(bytes(filename,'utf8'), 'rb') as f:
    file_content = f.read()

# Print first 10 lines
print('\n'.join(file_content.splitlines()[:10]))

# Test chunk decompression
decompressor = lzma.LZMADecompressor()

with lzma.open(bytes(filename,'utf8'), 'rb') as f:
    first_chunk = f.read(10)
    rest_of_file = decompressor.decompress(f.read())

complete_file = first_chunk + rest_of_file

# Print first 10 lines
print('\n'.join(complete_file.splitlines()[:10]))

# Test multiple decompressors
decompressor = lzma.LZMADecompressor()
with lzma.open(bytes(filename,'utf8'), 'rb') as f:
    first_part = decompressor.decompress(f.read(1000))
    second_part = decompressor.decompress
