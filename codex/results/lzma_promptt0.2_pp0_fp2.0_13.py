import lzma
# Test LZMADecompressor

# Test decompression of a file
def test_decompress_file():
    with open('test/testdata/lzma_compressed.xz', 'rb') as f_in:
        with lzma.open(f_in, 'rb') as f_out:
            assert f_out.read() == b'This is a test file.\n'

# Test decompression of a file with a preset
def test_decompress_file_preset():
    with open('test/testdata/lzma_compressed.xz', 'rb') as f_in:
        with lzma.open(f_in, 'rb', preset=9) as f_out:
            assert f_out.read() == b'This is a test file.\n'

# Test decompression of a file with a preset and filters
def test_decompress_file_preset_filters():
    with open('test/testdata/lzma_compressed.xz', 'rb') as f_in:
        with lzma.open(f
