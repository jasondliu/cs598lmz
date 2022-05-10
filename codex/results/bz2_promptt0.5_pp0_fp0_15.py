import bz2
# Test BZ2Decompressor
with bz2.BZ2File('data/example.bz2', 'rb') as f:
    print(f.read())

print('\n\n')

with bz2.BZ2File('data/example.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    text = decompressor.decompress(f.read())

print(text)

print('\n\n')

with bz2.BZ2File('data/example.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100), b''):
        text = decompressor.decompress(block)
        print(text)

print('\n\n')

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
print(compressor.compress(b'This is some text'))
print(compressor.flush())

print('\
