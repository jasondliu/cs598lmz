import lzma
lzma.open

# lzma has the same API as bz2 and zlib
# can use
# lzma.open() instead of
# open()
# to open an lzma-compressed file
 
# lzma.open()
# lzma.compress()
# lzma.decompress()

# lzma files typically have a .xz extension
 
# lzma is relatively new, and not widely used

# lzma is recommended for files that need to be compressed more than zlib and bz2 can manage

# lzma is typically several times better than bz2 at compressing files
