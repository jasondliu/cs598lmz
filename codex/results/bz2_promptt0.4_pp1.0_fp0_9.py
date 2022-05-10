import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as f:
    data = f.read()

decompressed_data = decompressor.decompress(data)

print(decompressed_data)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

compressed_data = compressor.compress(b'Hello World!')

# flush() is needed to get the last chunk of compressed data
compressed_data += compressor.flush()

print(compressed_data)

# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    data = f.read()

print(data)
 
# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    data = f.read()

print(data)

# Test BZ2File

with b
