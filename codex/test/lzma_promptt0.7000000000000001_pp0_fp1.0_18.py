import lzma
# Test LZMADecompressor objects

def test_decomp_state():
    """Test that the LZMADecompressor object can be pickled and
    unpickled."""
    # This test is inspired by issue #25506.

    data = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" * 100
    cdata = lzma.compress(data)
    co1 = lzma.LZMACompressor()
    co2 = lzma.LZMACompressor()
    cdata1 = co1.compress(data)
    cdata2 = co2.compress(data)
    cdata1 += co1.flush()
    cdata2 += co2.flush()
    assert cdata == cdata1 == cdata2
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        co1 = lzma.LZMACompressor()
        co2 = lzma.LZMACompressor()
        # Pickle the compressor object.
