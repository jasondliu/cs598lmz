import lzma
lzma.LZMAError

from lzma import *

# test the lzma module

def test_lzma():
    # test the lzma module
    data = b"1234567890abcdef" * 1024
    compressed = compress(data)
    decompressed = decompress(compressed)
    assert decompressed == data

    # test the LZMADecompressor class
    d = LZMADecompressor()
    assert d.decompress(compressed) == data
    assert d.unused_data == b""
    assert d.eof == True

    # test the LZMACompressor class
    c = LZMACompressor()
    assert c.compress(data) == compressed
    assert c.flush() == b""
    assert c.unused_data == b""

    # test the LZMADecompressor class with a stream
    d = LZMADecompressor()
    f = BytesIO(compressed)
    assert d.decompress(f.read(16)) == b""

