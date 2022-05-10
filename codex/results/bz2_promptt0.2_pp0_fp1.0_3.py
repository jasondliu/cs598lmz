import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('sample.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)
    print(decompressor.decompress(file_content))

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

uncompressed_data = b'This is the original text.'
compressed_data = compressor.compress(uncompressed_data)
tail = compressor.flush()

print(compressed_data)
print(tail)

decompressor = bz2.BZ2Decompressor()

decompressed_data = decompressor.decompress(compressed_data + tail)

print(decompressed_data)

# Test BZ2File

with bz2.BZ2File('sample.bz2', 'rb') as input:
    print(input.read())

with bz2.BZ2File('sample.bz2', 'wb')
