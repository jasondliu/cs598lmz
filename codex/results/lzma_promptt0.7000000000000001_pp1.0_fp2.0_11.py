import lzma
# Test LZMADecompressor
with open('lzma_compressed_file.xz', 'rb') as input:
    with lzma.open(input, 'rb') as output:
        decompressed_data = output.read()
        print('Output: %s' % decompressed_data)
        print('Original length: %s' % len(original_data))
        print('Decompressed length: %s' % len(decompressed_data))

# Test LZMACompressor
with open('lzma_compressed_file.xz', 'wb') as output:
    with lzma.open(output, 'w') as compressed:
        compressed.write(original_data)

# Test BZ2Compressor
with bz2.BZ2File('bz2_compress_file.bz2', 'wb') as output:
    with bz2.BZ2File('sample.csv', 'rb') as input:
        output.write(input.read())

# Test BZ2Decompressor
with bz2.BZ2File('bz2
