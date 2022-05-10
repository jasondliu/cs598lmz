import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('sample.bz2', 'rb') as f:
    file_content = f.read()
    print(decompressor.decompress(file_content))

with open('sample.bz2', 'rb') as f:
    for data in iter(lambda : f.read(100 * 1024), b''):
        print(decompressor.decompress(data))

with open('sample.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for data in iter(lambda : f.read(100 * 1024), b''):
        print(decompressor.decompress(data))

with open('sample.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    while True:
        block = f.read(100 * 1024)
        if not block:
            break
        print(decompressor.decompress(block))

with open('
