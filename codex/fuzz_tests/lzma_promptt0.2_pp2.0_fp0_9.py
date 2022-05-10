import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test that LZMADecompressor can decompress a file created with
    # xz -9.
    with open('lzma_compresslevel9.xz', 'rb') as f:
        compressed = f.read()
    with open('lzma_compresslevel9.txt', 'rb') as f:
        uncompressed = f.read()
    d = lzma.LZMADecompressor()
    assert d.decompress(compressed) == uncompressed
    assert d.unused_data == b''
    assert d.eof
    # Test that LZMADecompressor can decompress a file created with
    # xz -e.
    with open('lzma_extreme.xz', 'rb') as f:
        compressed = f.read()
    with open('lzma_extreme.txt', 'rb') as f:
        uncompressed = f.read()
    d = lzma.LZMADecompressor()
    assert d.
