import bz2
# Test BZ2Decompressor
# https://docs.python.org/3/library/bz2.html

decompressor = bz2.BZ2Decompressor()

with open('python.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)

uncompressed_data = decompressor.decompress(file_content)
print(uncompressed_data)

# Test BZ2Compressor
# https://docs.python.org/3/library/bz2.html

compressor = bz2.BZ2Compressor()

compressed_data = compressor.compress(b'Hello World!')
print(compressed_data)

compressed_data += compressor.flush()
print(compressed_data)

# Test bz2.open
# https://docs.python.org/3/library/bz2.html

with bz2.open('python.bz2', 'rt') as f:
    file_content = f.read()
    print(file_content)
 
