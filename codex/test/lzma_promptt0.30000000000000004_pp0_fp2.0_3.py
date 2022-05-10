import lzma
# Test LZMADecompressor

# Create a file with some data
with open("test.txt", "wb") as f:
    f.write(b"Hello world!\n" * 100)

# Compress the data
compressor = lzma.LZMACompressor()
with open("test.txt", "rb") as f_in, open("test.xz", "wb") as f_out:
    f_out.write(compressor.compress(f_in.read()))
    f_out.write(compressor.flush())

# Decompress the data
decompressor = lzma.LZMADecompressor()
with open("test.xz", "rb") as f_in, open("test.out", "wb") as f_out:
    f_out.write(decompressor.decompress(f_in.read()))

# Check if the output file is correct
