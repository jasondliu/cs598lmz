from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.decompress(data))

# Note that this is a "hack" and not a real solution
# If the file is small enough to fit into memory, you can just do
#  >>> data = open('file.bz2', 'rb').read()
#  >>> decomp = BZ2Decompressor().decompress(data)
#  >>> open('file', 'wb').write(decomp)
# Otherwise, you should use module bz2file (see the docs)
