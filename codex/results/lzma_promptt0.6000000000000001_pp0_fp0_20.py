import lzma
# Test LZMADecompressor by decompressing the first 10 bytes of the test data.
decompressor = lzma.LZMADecompressor()
decompressor.decompress(compressed_data[:10])

decompressor.flush()

# Test LZMACompressor by compressing the first 10 bytes of the test data.
compressor = lzma.LZMACompressor()
compressor.compress(data[:10])
compressor.flush()

# Test LZMAFile by compressing the test data and reading the compressed data
# back in again.
with lzma.open(data_filename, 'rb') as input, \
        lzma.open(compressed_filename, 'wb') as output:
    output.write(input.read())

with lzma.open(compressed_filename, 'rb') as input, \
        lzma.open(decompressed_filename, 'wb') as output:
    output.write(input.read())

with open(data_filename, 'rb') as f:
    assert f.read() == open(
