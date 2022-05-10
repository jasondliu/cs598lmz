import bz2
# Test BZ2Decompressor
print('Test BZ2Decompressor:')
decompressor = bz2.BZ2Decompressor()
decompressed_data = decompressor.decompress(compressed_data)
print(decompressed_data)

# Test BZ2File
print('Test BZ2File:')
with bz2.BZ2File('compressed_file.bz2', 'wb') as output:
    output.write(compressed_data)

with bz2.BZ2File('compressed_file.bz2', 'rb') as input:
    for line in input:
        print(line)
