import lzma
# Test LZMADecompressor with process_chunk().

def test_decompressobj_contextmanager():
    b = b"".join(b"a" * 100 for i in range(100))
    # Use the copy.copy trick to force the lzma module to create a new
    # LZMADecompressor object in the with statement.
    with lzma.decompressobj(format=lzma.FORMAT_XZ) as dec, \
         copy.copy(dec) as dec2:
        c = dec.compress(b)
        c += dec.flush()
        d = dec2.decompress(c)
        d += dec2.flush()
        assert d == b
        d = dec2.decompress(c)
        d += dec2.flush()
    assert d == b

def test_decompressobj_contextmanager_bad_format():
    b = b"".join(b"a" * 100 for i in range(100))
    # Use the copy.copy trick to force the lzma module to create a new
    # LZ
