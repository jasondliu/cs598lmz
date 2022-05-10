import bz2
bz2.decompress(f.read())

# Use gzip to read the compressed file.
f = gzip.open('example4.gz', 'rb')
f.read()

# Read using bz2.
f = bz2.BZ2File('example4.bz2', 'rb')
f.read()
