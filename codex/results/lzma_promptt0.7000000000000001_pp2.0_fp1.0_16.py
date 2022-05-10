import lzma
# Test LZMADecompressor
def test_lzma():
    # lzma is a wrapper around the basic LZMA compressor
    # LZMADecompressor is a wrapper around the basic LZMA decompressor
    # (see PEP 3151 for more details)
    cdata = lzma.compress(b'a' * 10 + b'b' * 10)
    d = lzma.LZMADecompressor()
    l = [d.decompress(cdata[:i]) for i in range(1, len(cdata))]
    assert b''.join(l) == b'a' * 10 + b'b' * 10

    d = lzma.LZMADecompressor()
    data = d.decompress(cdata)
    assert data == b'a' * 10 + b'b' * 10

# For the following tests, we need to use a known dict size.
# The dict size is stored in the first byte of the stream,
# which is then used by the decoder to initialize the dictionary
# (see Python/lzmam
