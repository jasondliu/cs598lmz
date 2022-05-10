import bz2
# Test BZ2Decompressor

def test_bz2_decompressor():
    # Test basic functionality
    d = bz2.BZ2Decompressor()
    eq_(d.decompress(bz2.compress(b"this is a test")), b"this is a test")
    eq_(d.flush(), b"")
    # Test multiple calls to decompress()
    d = bz2.BZ2Decompressor()
    x = d.decompress(bz2.compress(b"this is a test"))
    eq_(x, b"this is a test")
    eq_(d.decompress(b""), b"")
    eq_(d.flush(), b"")
    # Test multiple calls to decompress() with unprocessed data
    d = bz2.BZ2Decompressor()
    x = d.decompress(bz2.compress(b"this is a test"))
    eq_(x, b"this is a test")
