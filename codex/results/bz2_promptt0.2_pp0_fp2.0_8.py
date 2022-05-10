import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.open('example.bz2', 'rb') as input:
    with open('example.out', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

with open('example.out', 'rb') as input:
    original = input.read()

print(original == data)

# Test BZ2File

with bz2.open('example.bz2', 'rb') as input:
    with open('example.out', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(block)

with open('example.out', 'rb') as input:
    original = input.read()

print(original == data)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('
