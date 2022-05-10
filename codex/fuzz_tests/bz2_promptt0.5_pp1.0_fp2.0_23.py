import bz2
# Test BZ2Decompressor
data = open('./test.bz2', 'rb').read()
decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
print(compressor.compress(b'Hello World'))
print(compressor.flush())

# Test bz2.open
with bz2.open('./test.bz2', 'wt') as f:
    f.write('The same line, over and over.\n')

# Test BZ2File
with bz2.BZ2File('./test.bz2', 'wt') as f:
    f.write('The same line, over and over.\n')

# Test bz2.compress()
print(bz2.compress(b'The same line, over and over.\n'))

# Test bz2.decompress()
print(bz2.decompress(data))
