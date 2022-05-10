import lzma
# Test LZMADecompressor's ability to handle data that's not encoded with
# LZMA_CONCATENATED.
for i in range(1, 8):
    data = b'\x00' * i
    with pytest.raises(lzma.LZMAError):
        lzma.LZMADecompressor().decompress(data)
    assert lzma.LZMADecompressor(format=lzma.FORMAT_AUTO).decompress(
        data) == b''
    with pytest.raises(lzma.LZMAError):
        lzma.LZMADecompressor(format=lzma.FORMAT_RAW).decompress(data)
    with pytest.raises(lzma.LZMAError):
        lzma.LZMADecompressor(format=lzma.FORMAT_XZ).decompress(data)

# Test that LZMADecompressor raises an exception if data has a bad CRC32.
decomp = lzma.LZMADecomp
