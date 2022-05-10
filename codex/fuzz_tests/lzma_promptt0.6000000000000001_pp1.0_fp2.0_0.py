import lzma
# Test LZMADecompressor.

s = b'\0' * 1000 + b'x' * 1000

d = lzma.LZMADecompressor()

# Decompress some data.
d.decompress(s[:1000])

# Decompress the rest of the data.
d.decompress(s[1000:])

# No more data.
try:
    d.decompress(b'x')
except EOFError:
    pass

# Decompressor object can be used as a context manager.
with lzma.LZMADecompressor() as d:
    d.decompress(s)

# Decompress a file.
with open("testdata/empty.xz", "rb") as f:
    f.read()

with open("testdata/empty.xz", "rb") as f:
    lzma.decompress(f.read())

with open("testdata/empty.xz", "rb") as f:
    f.seek(0)
    lzma.decompress(
