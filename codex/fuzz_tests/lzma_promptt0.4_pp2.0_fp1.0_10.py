import lzma
# Test LZMADecompressor

def test_lzma_decompressor_init():
    lzma.LZMADecompressor()

def test_lzma_decompressor_decompress():
    d = lzma.LZMADecompressor()
    d.decompress(b'\x00')
    d.decompress(b'\x00')
    d.decompress(b'\x00')
    d.decompress(b'\x00')
    d.decompress(b'\x00')
    d.decompress(b'\x00')
    d.decompress(b'\x00')
    d.decompress(b'\x00')
    d.decompress(b'\x00')
    d.decompress(b'\x00')
    d.decompress(b'\x00')
    d.decompress(b'\x00')
    d.decompress(b'\x00')
    d.decompress(b'\x
