import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.BZ2File('data/sample.bz2', 'rb') as input:
    for block in iter(lambda: input.read(100*1024), b''):
        data = decompressor.decompress(block)
        if not data:
            break
        print(data)

decompressor.flush()

# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as input:
    for line in input:
        print(line)

# Test compress() and decompress()

uncompressed_data = b'The same line, over and over.\n' * 10
compressed_data = bz2.compress(uncompressed_data)

print(compressed_data)
print(bz2.decompress(compressed_data))

# Test compresslevel

for i in range(10):
    print('Compresslevel {}: {:6.2f} bytes'.format
