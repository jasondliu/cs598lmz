import bz2
# Test BZ2Decompressor
data = open('lorem.txt', 'rb').read()

print('Input contains %d bytes' % len(data))
print('First 100 bytes are: %r' % data[:100])

compressor = bz2.BZ2Compressor()
compressed = compressor.compress(data)
compressed += compressor.flush()

print('Compressed is %d bytes' % len(compressed))
print('First 100 bytes are: %r' % compressed[:100])

decompressor = bz2.BZ2Decompressor()
print(decompressed)
print(decompressed == data)

# The BZ2File class
# bz2.BZ2File(filename, mode='r', buffering=None, compresslevel=9)
with bz2.BZ2File('lorem.bz2', 'wb') as output:
    with open('lorem.txt', 'rb') as input:
        output.write(input.read())

with bz2.BZ2File('lorem.bz2', 'rb')
