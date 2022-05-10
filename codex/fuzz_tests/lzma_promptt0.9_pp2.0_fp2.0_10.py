import lzma
# Test LZMADecompressor
s = b"x" * 100 + lzma.compress(b"hello world")
c = lzma.LZMADecompressor()
c.decompress(s)

try:
	c.decompress(s[:6])
except OSError:
	print("OSError")

c.flush()

try:
	c.decompress(s[6:])
except OSError:
	print("OSError")

# Test xz decompression
c = lzma.LZMADecompressor()
print((c.decompress(lzma.compress(b"1234567890"))))

# Test bounds checking
c = lzma.LZMADecompressor()
try:
	c.decompress(lzma.compress(b"1234567890", format=lzma.FORMAT_ALONE))
except OSError:
	print("OSError")

try:
	c.decompress(lzma.compress(b"12345
