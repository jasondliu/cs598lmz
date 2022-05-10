import lzma
# Test LZMADecompressor

# Test that the decompressor can decompress a file
def test_decompress_file():
    with open('test_files/lzma_compressed_file.xz', 'rb') as f:
        compressed_data = f.read()
    decompressor = lzma.LZMADecompressor()
    decompressed_data = decompressor.decompress(compressed_data)
    with open('test_files/lzma_decompressed_file', 'rb') as f:
        assert decompressed_data == f.read()

# Test that the decompressor can decompress a string
def test_decompress_string():
    with open('test_files/lzma_compressed_string.xz', 'rb') as f:
        compressed_data = f.read()
    decompressor = lzma.LZMADecompressor()
    decompressed_data = decompressor.decompress(compressed_data)
