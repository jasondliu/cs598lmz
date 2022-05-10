import lzma
# Test LZMADecompressor with stream

def test_lzma():
    data = b"1234567890" * 100
    for level in range(10):
        with lzma.open(BytesIO(data), "w", preset=level) as f:
            f.write(data)
        with lzma.open(BytesIO(data)) as f:
            assert f.read() == data

# Test LZMADecompressor with small data

def test_lzma_small():
    data = b"1234567890" * 10
    with lzma.open(BytesIO(data), "w") as f:
        f.write(data)
    with lzma.open(BytesIO(data)) as f:
        assert f.read() == data

# Test LZMADecompressor with empty data

def test_lzma_empty():
    with lzma.open(BytesIO(), "w") as f:
        f.write(b"")
    with lzma.open(BytesIO()) as f:
        assert f.read
