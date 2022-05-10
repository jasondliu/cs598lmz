import lzma
# Test LZMADecompressor's max_length parameter.
# The data is a big string of 'x' characters, compressed with
# lzma.LZMACompressor(format=lzma.FORMAT_ALONE).
# The decompressor should raise an exception if the max_length
# parameter is too small.
data = open('lzma_alone.xz', 'rb').read()
decomp = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
decomp.decompress(data, max_length=1)

# The decompressor should not raise an exception if the max_length
# parameter is large enough.
decomp.decompress(data, max_length=len(data))

# The decompressor should return the correct data.
assert decomp.decompress(data) == b'x' * len(data)

# The decompressor should raise an exception if the max_length
# parameter is too small.
decomp.decompress(data, max_length=len(data) - 1)

# Test the decompressor's unused_
