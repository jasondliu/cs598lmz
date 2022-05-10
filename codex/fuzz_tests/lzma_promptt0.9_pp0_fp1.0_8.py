import lzma
# Test LZMADecompressor/Compressor class
buf = bytearray(b"foo bar baz foo bar baz foo bar baz foo bar baz")

for level in range(10):
    comp = lzma.LZMACompressor(format=lzma.FORMAT_RAW, filters=None, level=level)
    compbuf = memoryview(comp.compress(buf))
    assert (compbuf[:4] == b'\x00\x00\x00\x00')
    assert (compbuf[4:] == lzma.compress(buf, format=lzma.FORMAT_RAW, filters=None, level=level))
    assert (compbuf == lzma.compress(buf, format=lzma.FORMAT_AUTO, filters=None, level=level))

    dec = lzma.LZMADecompressor()
    dec.decompress(compbuf)
    assert dec.decompress(b"") == buf
