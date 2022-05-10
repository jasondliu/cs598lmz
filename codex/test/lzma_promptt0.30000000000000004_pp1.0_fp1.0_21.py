import lzma
# Test LZMADecompressor

# Compress the data
compressor = lzma.LZMACompressor()
compressed = compressor.compress(b"Hello world!")
compressed += compressor.flush()

# Decompress the data
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

# Check that the decompressed data is the same as the original
assert decompressed == b"Hello world!"
 
# Test LZMAFile

# Compress the data
with lzma.open("compressed.xz", "w") as fout:
    fout.write(b"Hello world!")

# Decompress the data
with lzma.open("compressed.xz") as fin:
    text = fin.read()

# Check that the decompressed data is the same as the original
assert text == b"Hello world!"
 
# Test LZMAStreamReader

# Compress the data
compressor = lzma.LZMACompressor()
