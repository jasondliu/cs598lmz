import bz2
bz2_data = bz2.compress(data)
len(bz2_data)

# bz2 compressed data takes less space then zlib

a = io.BytesIO()
bz_file = bz2.BZ2File(a, 'w')
bz_file.write(data)
bz_file.close()
print(len(a.getvalue()))


import gzip
s = io.BytesIO()
gz_file = gzip.GzipFile(fileobj=s, mode='w')
gz_file.write(data)
gz_file.close()
len(s.getvalue()) # gzip is slightly better compression rate

# Compression libraries are convenient because they support processing data
# in large chunks, which is critical for working with data streams.

# Reading and writing files in gzip or bz2 format
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

with bz2.open('somefile.bz2', 'rt') as f:
    text = f
