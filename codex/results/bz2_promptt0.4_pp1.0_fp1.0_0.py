import bz2
# Test BZ2Decompressor

with open('data/sample.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * decompressor.decompress(f.read(100))), b''):
        print(block)

# Test BZ2File

with bz2.BZ2File('data/sample.bz2') as f:
    for line in f:
        print(line)

# Test compress and decompress

original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)
compressed = bz2.compress(original_data)
print('Compressed   :', len(compressed), compressed)
decompressed = bz2.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)
