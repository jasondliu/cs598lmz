import lzma
# Test LZMADecompressor.eof
# Decompress a stream of lzma data
decompressor = lzma.LZMADecompressor()
compr = b'X' * 16 * 1024 + lzma.compress(b"foo") + b'X' * 16 * 1024
decomp = b''

while compr and not decompressor.eof:
    chunk = compr[:1024]
    compr = compr[1024:]
