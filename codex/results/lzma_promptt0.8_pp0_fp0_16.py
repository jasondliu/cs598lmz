import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
decomp.decompress(b"")
decomp.decompress(b"a")
decomp.decompress(b"ab")
decomp.decompress(b"foobar")
decomp.decompress(b"foo")
decomp.decompress(b"bar")
decomp.decompress(b"f" * 1000)
decomp.decompress(b"foobar" * 100)
decomp.decompress(b"foo" * 1000)
decomp.decompress(b"bar" * 1000)
decomp.finish()
try:
    decomp.decompress(b"foo")
except IOError:
    pass
# Test LZMADecompressor.decompress() with unbounded input
decomp = lzma.LZMADecompressor()
decomp.decompress(b"foo")
decomp.decompress(b"bar", max_length=7)
decomp.decompress(b"foobar
