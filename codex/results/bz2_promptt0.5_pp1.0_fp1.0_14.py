import bz2
# Test BZ2Decompressor
with bz2.open('./data/sample.bz2', 'rt') as f:
    data = f.read()
data

# BZ2Compressor
with bz2.open('./data/sample.bz2', 'wt') as f:
    f.write(data)
    
# BZ2File
with bz2.open('./data/sample.bz2', 'rt') as f:
    data = f.read()
data

# BZ2File
with bz2.open('./data/sample.bz2', 'wt') as f:
    f.write(data)

# Compressor and Decompressor
c = bz2.BZ2Compressor()
d = bz2.BZ2Decompressor()
c.compress(b'Hello World')
c.flush()
d.decompress(c.compress(b'Hello World'))
d.decompress(c.flush())
 
# Compressor and Decompressor
c = bz2.BZ2
