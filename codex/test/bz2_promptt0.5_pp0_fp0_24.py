import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('example.bz2', 'rb') as input:
    with open('uncompressed.txt', 'wb') as output:
        while True:
            block = input.read(100000)
            if not block:
                break
            output.write(decompressor.decompress(block))

print(open('uncompressed.txt').read())

# Test BZ2File

with bz2.BZ2File('example.bz2', 'rb') as input:
    with open('uncompressed.txt', 'wb') as output:
        while True:
            block = input.read(100000)
            if not block:
                break
            output.write(block)

print(open('uncompressed.txt').read())

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

