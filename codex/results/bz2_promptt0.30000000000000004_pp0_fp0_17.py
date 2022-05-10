import bz2
# Test BZ2Decompressor

with open('data/sample.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * 1024), b''):
        data = decompressor.decompress(block)
        if data:
            print(data)

# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    for line in f:
        print(line)
 
# Test compress and decompress

uncompressed_data = b'This is some uncompressed data.'
compressed_data = bz2.compress(uncompressed_data)
print(compressed_data)
decompressed_data = bz2.decompress(compressed_data)
print(decompressed_data)
 
# Test compresslevel

compressed_data = bz2.compress(uncompressed_data, compresslevel=9)
print(compressed_data)
decompressed_data = b
