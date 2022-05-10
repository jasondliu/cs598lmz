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
