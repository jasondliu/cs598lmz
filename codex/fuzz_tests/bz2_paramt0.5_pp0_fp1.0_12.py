from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed)

# We can also use the context manager to work with files.
with BZ2File('compressed-text.bz2', 'wb') as f:
    f.write(text)

with BZ2File('compressed-text.bz2', 'rb') as f:
    print(f.read())

# The module also includes a convenience function for calling compress()
# and decompress() with the least boilerplate.
import bz2
bz2.compress(text)
bz2.decompress(compressed)

# The bz2 module is a fairly thin wrapper over the libbz2 compression library.
# The library is not very convenient to use, but it is very efficient and works
# with a wide variety of compression algorithms.
