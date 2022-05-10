import bz2
# Test BZ2Decompressor
data = open('lorem.txt', 'rb').read()

print('Input contains %d bytes' % len(data))
print('First 100 bytes are: %r' % data[:100])

compressor = bz2.BZ2Compressor()
compressed = compressor.compress(data) + compressor.flush()

print('Compressed is %d bytes' % len(compressed))
print('First 100 bytes are: %r' % compressed[:100])

decompressor = bz2.BZ2Decompressor()
decompressed = decompressor.decompress(compressed)

print('Decompressed is %d bytes' % len(decompressed))
print('First 100 bytes are: %r' % decompressed[:100])

# Test BZ2File
filename = 'lorem.txt.bz2'
with bz2.BZ2File(filename, 'wb') as output:
    with open('lorem.txt', 'rb') as input:
        output.writelines(input)
