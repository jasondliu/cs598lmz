from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(data))

# bz2.BZ2File is a file-like object that compresses and decompresses data
# with bzip2 compression, which is usually faster and more efficient than gzip.
# bz2.BZ2File is a subclass of io.BufferedIOBase
with BZ2File('foo.bz2', 'rb') as input:
    print(input.read())

with BZ2File('foo.bz2', 'wb') as output:
    output.write(b"Hello World!\n")

# bz2.open() is a context manager that automatically opens and closes files
with bz2.open('foo.bz2', 'rt') as input:
    print(input.read())

with bz2.open('foo.bz2', 'wt') as output:
    output.write("Hello World!\n")

# One-liner to compress and decompress a string
bz2.decompress(bz2.compress(data))

# bz2.
