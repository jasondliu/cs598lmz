import lzma
# Test LZMADecompressor
data = b"xxxxxxxyyyyy" * 100000
comp = lzma.LZMACompressor()
compressed = comp.compress(data)
compressed += comp.flush()

decomp = lzma.LZMADecompressor()
assert decomp.decompress(compressed) == data


# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
decomp.decompress(compressed)
buffer = bytearray()
buffer.extend(decomp.unused_data)
try:
    decomp.decompress(b"")
except EOFError:
    pass
buffer.extend(decomp.unused_data)
assert buffer == data, len(buffer)

# Test LZMADecompressor with max_length
decomp = lzma.LZMADecompressor()
max_length = len(data) // 2
buffer = bytearray()
buffer.extend(decomp.decompress(compressed, max_length))
try:
