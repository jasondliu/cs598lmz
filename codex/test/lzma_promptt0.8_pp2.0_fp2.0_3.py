import lzma
# Test LZMADecompressor
def test_lzma_decompressor(input_file, size):
    # Read compressed file
    with open(input_file, 'rb') as f:
        data = f.read()

    decompressor = lzma.LZMADecompressor()
    out = decompressor.decompress(data, size)
    print(out)


# Test LZMADecompressor with context manager
def test_lzma_decompressor_2(input_file, size):
    # Read compressed file
    with open(input_file, 'rb') as f:
        data = f.read()

    with lzma.LZMADecompressor() as decompressor:
        out = decompressor.decompress(data, size)
        print(out)


# Test streaming decompression
def test_lzma_decompressor_3(input_file, size):
    with open(input_file, 'rb') as f:
        decompressor = lzma.LZMADecompressor()
        # Read one byte at a time
