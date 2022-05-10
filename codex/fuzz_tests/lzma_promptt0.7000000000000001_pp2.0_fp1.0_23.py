import lzma
# Test LZMADecompressor with data in multiple chunks.

def test_lzma_multi_chunk():
    # Test LZMADecompressor with data in multiple chunks.
    source = io.BytesIO(lzma.compress(b"Hello, world!"))
    decompressor = lzma.LZMADecompressor()
    result = b""
    while True:
        data = source.read(5)
        if not data:
            break
        result += decompressor.decompress(data)
    result += decompressor.flush()
    assert result == b"Hello, world!"

if __name__ == "__main__":
    test_lzma_multi_chunk()
