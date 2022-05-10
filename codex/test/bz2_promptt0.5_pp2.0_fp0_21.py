import bz2
# Test BZ2Decompressor.eof

def test_eof():
    # Test that eof returns the correct value
    data = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    d = bz2.BZ2Decompressor()
    assert d.eof == True
    d.decompress(data[:10])
    assert d.eof == False
    d.decompress(data[10:20])
    assert d.eof == False
    d.decompress(data[20:])
    assert d.eof == True
    d.decompress(b'blah')
    assert d.eof == True
    d.decompress(b'blah', True)
    assert d.eof == True

# Test that BZ2Decompressor objects can be copied

