import lzma
# Test LZMADecompressor.__init__()

def test_init():
    lz = lzma.LZMADecompressor()
    if not hasattr(lz, 'decompress'):
        raise Exception("LZMADecompressor has no decompress() method")
    if not hasattr(lz, 'flush'):
        raise Exception("LZMADecompressor has no flush() method")

def test_init_format():
    for format in lzma.FORMATS:
        lz = lzma.LZMADecompressor(format=format)
        if not hasattr(lz, 'decompress'):
            raise Exception("LZMADecompressor has no decompress() method")
        if not hasattr(lz, 'flush'):
            raise Exception("LZMADecompressor has no flush() method")

