import lzma
# Test LZMADecompressor

# Test the decompression of a file
def test_decompress_file():
    with lzma.open('test.xz') as f:
        data = f.read()
        assert data == b"Hello, world!\n"

# Test the decompression of a file with a custom filter chain
def test_decompress_file_custom_filter_chain():
    with lzma.open('test.xz', filters=[{"id": lzma.FILTER_LZMA2, "preset": 3}]) as f:
        data = f.read()
        assert data == b"Hello, world!\n"

# Test the decompression of a file with a custom filter chain
def test_decompress_file_custom_filter_chain_with_dict_size():
    with lzma.open('test.xz', filters=[{"id": lzma.FILTER_LZMA2, "preset": 3, "dict_size": 2**20}]) as f:
        data = f.read()
