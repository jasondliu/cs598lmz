import lzma
# Test LZMADecompressor

test_data = lzma.compress(b"hello world!")
test_data = b"".join(
    bytes([i]) for i in range(1, len(test_data) + 1)
) + test_data

dec = lzma.LZMADecompressor()

# Check the context manager works
with lzma.LZMADecompressor() as dec:
    assert dec.decompress(test_data) == b"hello world!"

# Check the object works
assert dec.decompress(test_data) == b"hello world!"

assert dec.unused_data == b""

dec.decompress(b"hello")
assert dec.unused_data == b"hello"

dec.decompress(b"")
assert dec.unused_data == b"hello"

# Check the object works after reset
dec.reset()
assert dec.decompress(test_data) == b"hello world!"

assert dec.unused_data == b""
import lzma

def test
