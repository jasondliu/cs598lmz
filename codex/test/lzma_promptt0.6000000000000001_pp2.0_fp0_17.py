import lzma
# Test LZMADecompressor.
c = lzma.LZMADecompressor()

with lzma.open("test.xz", "rb") as f:
    file_content = f.read()
