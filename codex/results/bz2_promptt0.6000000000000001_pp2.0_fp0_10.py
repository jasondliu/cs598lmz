import bz2
# Test BZ2Decompressor
with bz2.open('datasets/sample.bz2', 'rb') as source, open('sample.txt', 'w') as target:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: source.read(1024 * 1024), b''):
        target.write(decompressor.decompress(block))
# Test BZ2File
with bz2.open('datasets/sample.bz2') as s:
    content = s.read()
    print(content)

# Test BZ2Compressor
with open('sample.txt', 'rb') as source:
    compressor = bz2.BZ2Compressor()
    with open('sample.bz2', 'wb') as target:
        for block in iter(lambda: source.read(1024 * 1024), b''):
            target.write(compressor.compress(block))
        target.write(compressor.flush())

# Test BZ2Compressor.compress(data)
compressor = bz2.BZ2Comp
