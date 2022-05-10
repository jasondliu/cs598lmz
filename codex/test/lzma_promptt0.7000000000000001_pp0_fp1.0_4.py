import lzma
# Test LZMADecompressor

test_data = lzma.compress(b"hello world!")
test_data = b"".join(
    bytes([i]) for i in range(1, len(test_data) + 1)
) + test_data

dec = lzma.LZMADecompressor()

# Check the context manager works
