import lzma
# Test LZMADecompressor with a file
with open("data.xz", "rb") as f:
    with lzma.open(f, "rb") as xz_file:
        file_content = xz_file.read()
        print(file_content)

# Test LZMADecompressor with an input string
compressor = lzma.LZMACompressor()
data = b"Lots of data."
more_data = b"Even more data."
compressed = compressor.compress(data)
compressed += compressor.compress(more_data)
compressed += compressor.flush()
# print(compressed)

decompressor = lzma.LZMADecompressor()
decompressed_data = decompressor.decompress(compressed)
# print(decompressed_data)
