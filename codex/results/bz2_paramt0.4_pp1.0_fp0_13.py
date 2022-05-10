from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# To compress data, use the compress() method instead.
bz2_data = BZ2Compressor().compress(original_data)

# It’s also possible to use a BZ2Compressor object as a context manager.
with BZ2Compressor() as comp:
    for line in f:
        comp.compress(line)
    compressed_data = comp.flush()

# The bz2 module includes a utility function called bz2.open() that works like
# the built-in open() function, but automatically compresses or decompresses
# data as it is read or written.
with bz2.open('file.bz2', 'wt') as f:
    f.write(text)

with bz2.open('file.bz2', 'rt') as f:
    text = f.read()

# The bz2.open() function also accepts compression level as an optional keyword
# argument.
with bz2.open('file.bz2', 'wt', compresslevel=9)
