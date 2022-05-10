import lzma
# Test LZMADecompressor

# Create a compressed file
data = b'Some data'
lzmafile = BytesIO()
fs = lzma.LZMAFile(lzmafile, mode='w', format=lzma.FORMAT_RAW, filters=[{'id':lzma.FILTER_LZMA2, 'preset':3}])
fs.write(data)
fs.close()

# Decompress the data
fs = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
fs.decompress(lzmafile.getvalue())

# Check the decompressed data
fs.unconsumed_tail == data

# Decompress the data again
fs.decompress(lzmafile.getvalue())

# Check that the LZMADecompressor is in an error state
fs.eof

# Try to decompress the data again
fs.decompress(lzmafile.getvalue())

# Check that the LZMADecompressor is still in an error
