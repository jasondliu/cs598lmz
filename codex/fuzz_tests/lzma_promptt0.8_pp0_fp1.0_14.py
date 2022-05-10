import lzma
# Test LZMADecompressor.theDictionarySize
assert lzma.LZMADecompressor().theDictionarySize == 4096

# Check that we don't crash by trying to decompress garbage that has less than
# LZMA_HEADER_SIZE bytes.
comp = lzma.LZMADecompressor()
comp.decompress(b'x' * lzma.LZMA_HEADER_SIZE)

assert comp.decompress(b'x') == b''

# After the first EOS marker we must not raise BufferError when decompressing.
comp.decompress(b'\x00')
assert comp.decompress(b'x') == b''

# Test that a custom dictionary works.
comp = lzma.LZMADecompressor(lzma.FORMAT_RAW, None, b"abc")
comp.decompress(lzma.compress(b"abcdef"))
comp.decompress(lzma.compress(b"ghijkl"))
del comp

# Test that we can use the context manager protocol.
with
