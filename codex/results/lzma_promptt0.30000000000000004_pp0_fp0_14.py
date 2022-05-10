import lzma
# Test LZMADecompressor

# Compress
compressor = lzma.LZMACompressor()
compressed = compressor.compress(b"Hello World!")
compressed += compressor.flush()

# Decompress
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)

# Decompress with context manager
with lzma.LZMADecompressor() as decompressor:
    decompressed = decompressor.decompress(compressed)
    print(decompressed)

# Decompress with context manager and read data from file
with lzma.open("data.xz", "rb") as f:
    file_content = f.read()
    print(file_content)

# Decompress with context manager and write data to file
with lzma.open("data.xz", "rb") as f_in, open("data.txt", "wb") as f_out:
    f_out.write(f_in.read())

# Decomp
