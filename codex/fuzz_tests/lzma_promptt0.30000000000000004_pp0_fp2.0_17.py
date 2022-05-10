import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    with open('testdata/lzma.xz', 'rb') as f:
        with lzma.LZMADecompressor() as decomp:
            data = decomp.decompress(f.read())
    assert data == b'12345abcde\n'

# Test LZMADecompressor.decompress()

def test_lzma_decompressor_decompress():
    with open('testdata/lzma.xz', 'rb') as f:
        with lzma.LZMADecompressor() as decomp:
            data = decomp.decompress(f.read())
    assert data == b'12345abcde\n'

def test_lzma_decompressor_decompress_maxlength():
    with open('testdata/lzma.xz', 'rb') as f:
        with lzma.LZMADecompressor() as decomp:
            data = decomp.decompress(f.read(), max_length
