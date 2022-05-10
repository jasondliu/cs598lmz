import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

decompressed_data = decompressor.decompress(compressed_data)

print(decompressed_data)

# Test BZ2File

with bz2.BZ2File('sample.bz2', 'wb') as f:
    f.write(compressed_data)

with bz2.BZ2File('sample.bz2', 'rb') as f:
    print(f.read())
 
# Test BZ2File with context manager

with bz2.BZ2File('sample.bz2', 'wb') as f:
    f.write(compressed_data)

with bz2.BZ2File('sample.bz2', 'rb') as f:
    for line in f:
        print(line)
 
# Test BZ2File with context manager and readlines()

with bz2.BZ2File('sample.bz2', 'wb') as f:
    f.write(compressed_data
