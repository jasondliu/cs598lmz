import bz2
# Test BZ2Decompressor object API
decomp = bz2.BZ2Decompressor()

# Show what methods the decompressor object has
#print([method for method in dir(decomp) if callable(getattr(decomp, method))])

# Create a BZ2File object with mode='r'
# This will return a decompression stream
# bz2file is an iterable that produces bytes
