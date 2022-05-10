import bz2
# Test BZ2Decompressor

d = bz2.BZ2Decompressor()

with open('test.bz2', 'rb') as f:
    data = f.read()
    print(d.decompress(data))

# Test BZ2Compressor

c = bz2.BZ2Compressor()

with open('test.bz2', 'wb') as f:
    f.write(c.compress(b'Hello World'))
    f.write(c.flush())

# Test BZ2File

with bz2.BZ2File('test.bz2', 'w') as f:
    f.write(b'Hello World')

with bz2.BZ2File('test.bz2', 'r') as f:
    print(f.read())

# Test BZ2File with context manager

with bz2.BZ2File('test.bz2', 'w') as f:
    f.write(b'Hello World')

with bz2.BZ2File('test.bz
