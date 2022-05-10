import bz2
# Test BZ2Decompressor

f = bz2.BZ2File('example.bz2')
print(f.read())

f.close()

# Test BZ2Compressor

f = bz2.BZ2File('example.bz2', 'w')
f.write(b'Hello World')
f.close()

# Test BZ2Compressor

f = bz2.BZ2File('example.bz2', 'w')
f.write(b'Hello World')
f.close()

# Test BZ2Compressor

f = bz2.BZ2File('example.bz2', 'w')
f.write(b'Hello World')
f.close()

# Test BZ2Compressor

f = bz2.BZ2File('example.bz2', 'w')
f.write(b'Hello World')
f.close()

# Test BZ2Compressor

f = bz2.BZ2File('example.bz2', 'w')
