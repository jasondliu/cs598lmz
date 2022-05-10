import lzma
# Test LZMADecompressor

# Test decompression of a file
def test_decompress_file():
    with open('test/test.xz', 'rb') as f:
        decomp = lzma.LZMADecompressor()
        data = decomp.decompress(f.read())
        assert data == b'foobar'

# Test decompression of a file with a preset
def test_decompress_file_preset():
    with open('test/test.xz', 'rb') as f:
        decomp = lzma.LZMADecompressor(preset=9)
        data = decomp.decompress(f.read())
        assert data == b'foobar'

# Test decompression of a file with a filter chain
def test_decompress_file_filter_chain():
    with open('test/test.xz', 'rb') as f:
        decomp = lzma.LZMADecompressor(filters=[{'id': lzma.FILTER_LZMA2}])
        data = decomp.decompress(
