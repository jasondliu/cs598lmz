from bz2 import BZ2Decompressor
BZ2Decompressor().decompress()

def test_bz2_decompressor_decompress():
    # Test the decompressor decompress() method
    # check that an empty string is returned for an empty string
    assert BZ2Decompressor().decompress(b("")) == b("")
    # check that an empty string is returned for a short string
    assert BZ2Decompressor().decompress(b("BZh9")) == b("")
    # check that an exception is raised for bad data
    try:
        BZ2Decompressor().decompress(b("BZh91"))
    except IOError as e:
        assert e.args[0] == "invalid data stream"
    else:
        raise AssertionError("IOError not raised")
    # check that an exception is raised when the compressed data ends
    # before the end of the first member
    try:
        BZ2Decompressor().decompress(b("BZh9\x01"))
    except EOFError as e:
        assert e.args[0] == "comp
