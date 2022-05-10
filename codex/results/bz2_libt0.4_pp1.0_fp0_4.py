import bz2
bz2.decompress(compressed_data)

# compress a file
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

# decompress a file
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

# compress a file
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

# decompress a file
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()

# compress a file
with lzma.open('somefile.xz', 'wt') as f:
    f.write(text)

# decompress a file
with lzma.open('somefile.xz', 'rt') as f:
    text = f.read()

# compress a file
with zlib.open('somefile.zz', 'wt') as f:
    f.write(text)

# decompress a file

