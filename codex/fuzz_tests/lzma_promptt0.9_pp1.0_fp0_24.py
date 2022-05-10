import lzma
# Test LZMADecompressor module
comp = lzma.LZMACompressor()
comp_data = b''.join(comp.compress(data) for data in [b"foo", b"bar"])
comp_data += comp.flush()
assert lzma.LZMADecompressor().decompress(comp_data) == b'foobar'
# Test LZMACompressor/LZMADecompressor
buf = io.BytesIO()
with lzma.LZMACompressor(format=lzma.FORMAT_XZ) as comp:
    comp.chunksize = 13
    comp.write(b"abc")
    comp.write(b"defg")
    comp.write(b"h")
    comp.write(b"ijk")
    comp.flush(lzma.RUN_FINISH)
    buf.write(comp.buffer)
    if comp.buffered_size != 0:
        raise Exception("unexpected buffered_size")
buf.seek(0)
with lzma.LZMADecompressor() as dec:

