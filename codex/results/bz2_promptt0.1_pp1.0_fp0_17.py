import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as f:
    file_content = f.read()
    print(decompressor.decompress(file_content))

# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    print(f.read())

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/sample.bz2', 'rb') as f:
    file_content = f.read()
    compressed_content = compressor.compress(file_content)
    compressed_content += compressor.flush()

with open('data/sample_compressed.bz2', 'wb') as f:
    f.write(compressed_content)

# Test BZ2File

with bz2.BZ2File('data/sample_compressed.bz2', 'wb') as f:
    f.
