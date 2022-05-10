import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.open('example.bz2', 'rb') as input:
    with open('example.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

print(open('example.txt', 'rt').read())

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('example.txt', 'rb') as input:
    with bz2.open('example.bz2', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(compressor.compress(block))
        output.write(compressor.flush())

print(open('example.bz2', 'rb').read())

# Test BZ2File

with bz2.open('example.bz2', 'rt')
