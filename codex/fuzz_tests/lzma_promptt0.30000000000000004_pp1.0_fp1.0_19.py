import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # This is a test for issue #17092
    # It's not clear how to test it better, but at least it should not crash
    lzc = lzma.LZMADecompressor()
    lzc.decompress(b"")
    lzc.flush()
    lzc.decompress(b"")
    lzc.flush()
    lzc.decompress(b"")
    lzc.flush()
    lzc.decompress(b"")
    lzc.flush()

def test_lzma_decompressor_reset():
    lzc = lzma.LZMADecompressor()
    lzc.decompress(b"")
    lzc.flush()
    lzc.reset()
    lzc.decompress(b"")
    lzc.flush()
    lzc.reset()
    lzc.decompress(b"")
    lz
