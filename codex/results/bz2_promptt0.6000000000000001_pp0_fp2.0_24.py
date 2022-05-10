import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.BZ2File('data.bz2', 'rb') as input:
    with open('uncompressed.txt', 'wb') as output:
        for data in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(data))

print(open('uncompressed.txt', 'rt').read())

# Test BZ2Compressor

compressor = bz2.BZ2Compressor(9)

with open('uncompressed.txt', 'rb') as input:
    with bz2.BZ2File('compressed.bz2', 'wb', compresslevel=9) as output:
        output.write(input.read())

print(open('compressed.bz2', 'rb').read())

# Test BZ2File

with bz2.BZ2File('data.bz2', 'rb') as input:
    print(input.read())

with b
