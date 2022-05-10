import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    # Test decompression using the decompressor object.
    cdata = lzma.compress(b"Testing the LZMADecompressor object")
    d = lzma.LZMADecompressor()
    data = b""
    for i in range(0, len(cdata), 16):
        data += d.decompress(cdata[i:i+16])
    data += d.flush()
    assert data == b"Testing the LZMADecompressor object"

def test_lzma_decompressor_reset():
    # Test decompression using the decompressor object.
    cdata = lzma.compress(b"Testing the LZMADecompressor object")
    d = lzma.LZMADecompressor()
    data = d.decompress(cdata)
    d.reset()
    data += d.decompress(cdata)
    data += d.flush()
