import lzma
# Test LZMADecompressor class
s = b'\x00' * 256 * 1024 + b'12345678abcdef'
d = lzma.LZMADecompressor()

d.decompress(s[:512])
