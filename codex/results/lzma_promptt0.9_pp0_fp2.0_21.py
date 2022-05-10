import lzma
# Test LZMADecompressor

# Test compress method
compressor = lzma.LZMACompressor(format=lzma.FORMAT_ALONE)
compr_data = compressor.compress(bytes(1000000)) 
compr_data += compressor.flush()


# Test decompress method
NEW_DATA = b'JABBERWOCKY'
compressor = lzma.LZMACompressor(format=lzma.FORMAT_ALONE)

# Get compressed data and append new data
compr_data = compressor.compress(compr_data)
compr_data += compressor.flush()

# Decompress everything
decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)

# Decompress data
decompr_data = decompressor.decompress(compr_data)

# Check data
assert(decompr_data == compr_data[:-len(NEW_DATA)] + NEW_DATA)

# Decompress with max_length=-1
decompressor = lzma.L
