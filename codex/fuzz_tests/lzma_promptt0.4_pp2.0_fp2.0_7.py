import lzma
# Test LZMADecompressor

def test_decompressor_no_data():
    decompressor = lzma.LZMADecompressor()

    # Calling decompress() with no data should raise an exception.
    with pytest.raises(EOFError):
        decompressor.decompress(b"")

    # Calling flush() with no data should raise an exception.
    with pytest.raises(EOFError):
        decompressor.flush()


def test_decompressor_unused_data():
    decompressor = lzma.LZMADecompressor()

    # Calling decompress() with unused data should raise an exception.
    with pytest.raises(ValueError):
        decompressor.decompress(b"\x00" * 100)

    # Calling flush() with unused data should raise an exception.
    with pytest.raises(ValueError):
        decompressor.flush()


def test_decompressor_with_eof():
    decompressor = lzma.LZMADecompressor()

    # Calling decompress() with EOF should return
