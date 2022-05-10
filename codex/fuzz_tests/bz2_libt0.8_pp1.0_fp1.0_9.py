import bz2
bz2.compress('bread.png')

# Method 2
f = open('bread.png')
data = f.read()
f.close()
compressed = bz2.compress(data)

# Method 3
f = open('bread.png')
data = f.read()
f.close()
compressed = bz2.compress(data)
len(data)
len(compressed)

# BZ2 decompression
bz2.decompress(compressed)

# Method 2
f = open('bread.bz2', 'wb')
f.write(compressed)
f.close()

# Method 3
f = open('bread.bz2', 'wb')
f.write(compressed)
f.close()
f = bz2.BZ2File('bread.bz2', 'wb')
f.write(data)
f.close()

# GZIP compression
import gzip
f = gzip.open('bread.gz', 'wb')
f.write(data)
f.close()

#
