import bz2
# Test BZ2Decompressor

with open('/Users/jason/Downloads/sample.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * 1024), b''):
        print(decompressor.decompress(block))

# Test BZ2File

with bz2.BZ2File('/Users/jason/Downloads/sample.bz2', 'rb') as f:
    for line in f:
        print(line)

# Test open()

with bz2.open('/Users/jason/Downloads/sample.bz2', 'rt') as f:
    for line in f:
        print(line)

# Test compress()

with open('/Users/jason/Downloads/sample.txt', 'rb') as f:
    data = f.read()
    compressed = bz2.compress(data)
    print(compressed)

# Test decompress()

with open('/Users/jason/Download
