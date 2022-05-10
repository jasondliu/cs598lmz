import lzma
# Test LZMADecompressor module
comp = lzma.LZMACompressor()
comp_data = b''.join(comp.compress(data) for data in [b"foo", b"bar"])
comp_data += comp.flush()
assert lzma.LZMADecompressor().decompress(comp_data) == b'foobar'
# Test LZMACompressor/LZMADecompressor
