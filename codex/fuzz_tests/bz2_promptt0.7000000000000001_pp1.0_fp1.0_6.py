import bz2
# Test BZ2Decompressor
with bz2.BZ2Decompressor() as decompressor:
    with open('./data/sample.bzip2', 'rb') as f:
        file_content = f.read()
        decompressed_data = decompressor.decompress(file_content)
        print('Decompressed is {} bytes'.format(len(decompressed_data)))

        with open('./data/sample.csv', 'wb') as f:
            f.write(decompressed_data)


# Test BZ2Compressor
with open('./data/sample.csv') as input:
    with bz2.BZ2File('./data/sample.bzip2', 'w') as output:
        compress_data = input.read()
        compress_data = compress_data.encode('utf-8')
        compressor = bz2.BZ2Compressor()
        compressor.compress(compress_data)
        output.write(compressor.flush())
