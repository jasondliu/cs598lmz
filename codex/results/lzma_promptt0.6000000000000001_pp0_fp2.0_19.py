import lzma
# Test LZMADecompressor class
s = b'\x00' * 256 * 1024 + b'12345678abcdef'
d = lzma.LZMADecompressor()

d.decompress(s[:512])
d.decompress(s[512:1024])
d.decompress(s[1024:])
d.flush()


# Test LZMADecompressor class with multiple decompress() calls
s = b'\x00' * 256 * 1024 + b'12345678abcdef'
d = lzma.LZMADecompressor()
d.decompress(s, len(s))
d.flush()


# Test LZMADecompressor class with multiple decompress() calls
s = b'\x00' * 256 * 1024 + b'12345678abcdef'
d = lzma.LZMADecompressor()
d.decompress(s, len(s) - 1)
d.flush()


# Test LZMADecompressor class with multiple decompress() calls
s = b'\x00
