import bz2
# Test BZ2Decompressor
data = open('lorem.txt', 'rb').read()
decompressor = bz2.BZ2Decompressor()
for chunk in generate_chunks(data):
    print(decompressor.decompress(chunk), end='')

print()

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
for chunk in generate_chunks(data):
    print(compressor.compress(chunk), end='')
print(compressor.flush())

print()

# Test incremental compression with default compressor
compressor = bz2.BZ2Compressor()
with open('lorem.txt.bz2', 'wb') as f:
    for chunk in generate_chunks(data):
        f.write(compressor.compress(chunk))
    f.write(compressor.flush())

# Test file decompression
with bz2.open('lorem.txt.bz2') as input, open('lorem.uncompressed.txt', 'w') as output:
    for line
