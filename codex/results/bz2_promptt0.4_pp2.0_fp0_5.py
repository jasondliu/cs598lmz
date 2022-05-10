import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('sample.bz2', 'rb') as f:
    file_content = f.read()
    print(file_content)
    print(decompressor.decompress(file_content))

with open('sample.bz2', 'rb') as f:
    for block in iter(lambda: f.read(100), b''):
        print(decompressor.decompress(block))

with open('sample.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100), b''):
        print(decompressor.decompress(block))

with open('sample.bz2', 'rb') as f:
    for block in iter(lambda: f.read(100), b''):
        print(decompressor.decompress(block))
        decompressor = bz2.BZ2Decompressor()

with open('sample.bz
