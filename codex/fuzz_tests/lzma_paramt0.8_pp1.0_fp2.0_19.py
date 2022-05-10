from lzma import LZMADecompressor
LZMADecompressor().decompress(b"\xfd\x37\x7a\x58\x5a\x00\x00\x00\x04\x00\x00\xff\xff")

# Example 6.11. Compressing Data in Streaming Mode with lzma
with lzma.open("lorem-compressed.xz", "wt") as f:
    f.write(LOREM)
with lzma.open("lorem-compressed.xz", "rt") as f:
    text = f.read()
text

# Example 6.12. Compressing Data When Writing to a File
with open("lorem-compressed.xz", "wb") as f:
    f.write(lzma.compress(LOREM.encode("utf-8")))

with open("lorem-compressed.xz", "rb") as f:
    data = f.read()
data

lzma.decompress(data).decode("utf-8")

# Example 6.13. Using a Compression Parameters Object
comp
