import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, decompress it, and write the result
with open('compressed_file.xz', 'rb') as in_file, open('uncompressed_file', 'wb') as out_file:
    while True:
        buf = in_file.read(1)
        if not buf:
            break
        result = decompressor.decompress(buf)
        if result:
            out_file.write(result)

# Flush the decompressor to get any remaining data
result = decompressor.flush()
if result:
    out_file.write(result)
 
# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Compress some data
data = b'This is the data to compress. It is not very long so the compression ratio will suffer'
compressed = compressor.compress(data)
# Write any remaining data to the output file
compressed += compressor.flush()
