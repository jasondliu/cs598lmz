import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as input:
    with open('data/sample.out', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(decompressor.decompress(block))

# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as input:
    with open('data/sample.out', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(block)

# Test BZ2File with context manager

with bz2.BZ2File('data/sample.bz2', 'rb') as input, open('data/sample.out', 'wb') as output:
    while True:
        block = input.read(1024)
        if not block:
            break
        output.write
