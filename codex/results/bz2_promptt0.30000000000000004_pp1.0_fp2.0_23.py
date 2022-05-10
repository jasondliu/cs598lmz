import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100)
    print(decompressor.decompress(data))

with open('data/enwik8.bz2', 'rb') as f:
    for chunk in iter(lambda: f.read(100), b''):
        print(decompressor.decompress(chunk))
        break

with open('data/enwik8.bz2', 'rb') as f:
    for chunk in iter(lambda: f.read(100), b''):
        decompressor.decompress(chunk)
        break

print(decompressor.unused_data)

print(decompressor.eof)

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    for chunk in iter(lambda: f.read(100), b''):
        print
