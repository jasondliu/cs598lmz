import bz2
# Test BZ2Decompressor
data = open('lorem.txt', 'rb').read()

print('Input contains %d bytes' % len(data))
print('First 100 bytes are: %r' % data[:100])
print()

compressor = bz2.BZ2Compressor()
compressed = compressor.compress(data)
print('Compressed contains %d bytes' % len(compressed))
print('First 100 bytes are: %r' % compressed[:100])
print()

decompressor = bz2.BZ2Decompressor()
decompressed = decompressor.decompress(compressed)
print('Decompressed contains %d bytes' % len(decompressed))
print('First 100 bytes are: %r' % decompressed[:100])
print()

print('Decompressed matches original:', decompressed == data)

# Test BZ2File
with open('lorem.txt', 'rb') as input:
    with bz2.BZ2File('lorem.txt.bz2', 'wb') as output:
        for data in iter(
