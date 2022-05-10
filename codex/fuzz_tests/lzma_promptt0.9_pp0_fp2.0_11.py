import lzma
# Test LZMADecompressor.decompress(), which is not covered by the other tests.
for compressflag in (0, 2):
    c = lzma.LCompressor({'preset': compressflag})
    d = lzma.LZMADecompressor()
    data = bytes(bytearray(range(256)))
    compressed = c.compress(data)
    more_compressed = c.compress(b'')
    assert more_compressed == b''
    decompressed = d.decompress(compressed + more_compressed)
    assert decompressed == data
    assert not d.eof
    final = d.decompress(b'')
    assert final == b''
    assert d.eof
    # We can't run decompressor.decompress() after the eof flag is set.
    exc = raises(EOFError, d.decompress, b'blat')
    assert str(exc.value) == 'LZMA data is corrupt'
# Test with corrupt input data.
d = lzma.LZMADecompressor()

