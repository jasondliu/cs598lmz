import lzma
# Test LZMADecompressor parameters
decomp = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
decomp.decompress(b'Yvonne')

# Wrong format
decomp = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
try:
    decomp.decompress(b'Yvonne')
except lzma.LZMAError as err:
    print(err)

# Test filters
# The format alone does not have the filter headers
decomp = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE, filters=[])
try:
    decomp.decompress(b'Yvonne')
except lzma.LZMAError as err:
    print(err)

# The format auto will search for the filter header
decomp = lzma.LZMADecompressor(format=lzma.FORMAT_AUTO, filters=[])
try:
    decomp.decompress(b'Yvonne')

