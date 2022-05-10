import lzma
# Test LZMADecompressor
def test_lzma_decompressor():
    data = b'\x5d\x00\x00\x80\x00\xff'
    c = lzma.LZMADecompressor()
    c.decompress(data)
    c.decompress(b'\x03')
    c.decompress(b'\x04')
    c.decompress(b'\x05')
    c.decompress(b'\x06')
    c.decompress(b'\x07')
    c.decompress(b'\x08')
    c.decompress(b'\x09')
    c.decompress(b'\x0a')
    c.decompress(b'\x0b')
    c.decompress(b'\x0c')
    c.decompress(b'\x0d')
    c.decompress(b'\x0e')
    c.decompress(b'\x0f')
    c.dec
