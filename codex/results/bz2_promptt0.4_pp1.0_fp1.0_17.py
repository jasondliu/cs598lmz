import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
data = decompressor.decompress(compressed_data)

print('Decompressed is {} bytes'.format(len(data)))
print(data[:100].decode('utf-8'))

# Test BZ2File
with bz2.BZ2File('example.bz2', 'rb') as input:
    print(input.readline())

# Test BZ2File as a context manager
with bz2.BZ2File('example.bz2', 'rb') as input:
    for line in input:
        print(line)

# Test BZ2File with a compression level
with bz2.BZ2File('example.bz2', 'wb', compresslevel=9) as output:
    output.write(data)

# Test BZ2File with a file-like object
uncompressed_data = open('example.txt', 'rb').read()
with bz2.BZ2File('example.bz2', 'wb') as output:

