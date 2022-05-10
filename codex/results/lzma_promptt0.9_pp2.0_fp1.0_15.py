import lzma
# Test LZMADecompressor interface
def readall(x):
    while True:
        buf = x.decompress(b"a" * 100)
        if not buf:
            break
def readallerr(x):
    try:
        readall(x)
    except lzma.LZMAError as e:
        assert e.args == ('File not in the .xz format',)
    else:
        assert 0
d = lzma.LZMADecompressor()
readallerr(d)
d = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
readallerr(d)
d = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
readallerr(d)
d = lzma.LZMADecompressor(format=lzma.FORMAT_AUTO)
readallerr(d)
d.decompress(b"")
readallerr(d)
d.decompress(b"foo")
readallerr(d)
