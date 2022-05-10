import lzma
# Test LZMADecompressor.eof
# Decompress a stream of lzma data
decompressor = lzma.LZMADecompressor()
compr = b'X' * 16 * 1024 + lzma.compress(b"foo") + b'X' * 16 * 1024
decomp = b''

while compr and not decompressor.eof:
    chunk = compr[:1024]
    compr = compr[1024:]
    decomp += decompressor.decompress(chunk)

decomp += decompressor.flush()
print(decomp)
print(len(decomp))

# Test LZMADecompressor.unused_data
decompressor = lzma.LZMADecompressor()
print(decompressor.unused_data)

compr = lzma.compress(b"foo")
decompressor.decompress(compr)
print(decompressor.unused_data)

# Test LZMADecompressor.decompress() with too much data
decompressor = lzma.LZMAD
