import lzma
# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()

# The input file has to be opened in binary mode.
with open("test.xz", "rb") as input:
    # Read all the compressed data.
    data = input.read()

    # Decompress the data.
    decompressed_data = decompressor.decompress(data)
    print(decompressed_data)
