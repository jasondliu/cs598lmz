import lzma
# Test LZMADecompressor.get_decompress_size()

def test_decompress_size_ok(size):
    with lzma.LZMADecompressor() as dec:
        dec.decompress(b'X' * (size - 1))
        assert dec.get_decompress_size() == size


def test_decompress_size_invalid():
    with lzma.LZMADecompressor() as dec:
        dec.decompress(b'X' * 5)
        with pytest.raises(lzma.LZMAError):
            dec.get_decompress_size()


def test_decompress_size_ok_multiple_calls(size):
    with lzma.LZMADecompressor() as dec:
        dec.decompress(b'X' * (size - 1))
        for n in range(10):
            assert dec.get_decompress_size() == size


