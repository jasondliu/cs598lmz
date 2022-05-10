import lzma
# Test LZMADecompressor.decompress()

# Return uncompressed data from a lzma-compressed string.
# The `method` argument specifies method of compression.
# Returns the original string if compression is not possible due to
# the LZMAError exception.

def lzma_decompress(data, method=0):
    try:
        lz = lzma.LZMADecompressor()
        res = lz.decompress(data)
        return res
    except lzma.LZMAError:
        return data

# Test LZMADecompressor.decompress() with multiple calls.
# Requires previously defined `lzma_decompress()` function.

