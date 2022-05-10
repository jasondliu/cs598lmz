import bz2
# Test BZ2Decompressor
# Compress data
data = b'Lots of content here.'
compressor = bz2.BZ2Compressor()
compressed_data = compressor.compress(data)
compressed_data += compressor.flush()
print('Compressed is %d bytes' % len(compressed_data))
# Decompress data
decompressor = bz2.BZ2Decompressor()
decompressed_data = decompressor.decompress(compressed_data)
print('Decompressed is %d bytes' % len(decompressed_data))
print(decompressed_data)

# Test BZ2File
# Compress data
with bz2.BZ2File('example.bz2', 'wb') as output:
    for line in open('example.txt', 'rt'):
        output.write(line.encode('utf-8'))
# Decompress data
with bz2.BZ2File('example.bz2', 'rb') as input:
    for line in input:
        print(line.decode('utf-8').
