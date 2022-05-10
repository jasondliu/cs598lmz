import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('../data/sample.bz2', 'rb') as input:
    for block in iter(lambda: input.read(100 * 1024), b''):
        print(decompressor.decompress(block))

print('Is the decompressor at the end?', decompressor.eof)

# Test BZ2File

with bz2.BZ2File('../data/sample.bz2', 'r') as input:
    for line in input:
        print(line)

# Test BZ2File with context managers

with bz2.BZ2File('../data/sample.bz2', 'r') as input:
    print(input.readline())

# Test BZ2File with context managers

with bz2.BZ2File('../data/sample.bz2', 'r') as input:
    print(input.readline().decode('utf-8'))

# Test BZ2File with context managers

with bz
