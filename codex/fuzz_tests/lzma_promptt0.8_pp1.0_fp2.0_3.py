import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
with open("test_xz_bad_1.xz", "rb") as f:
    data = f.read()

decomp.decompress(data)
# Patch LZMADecompressor to return some data
decomp.decompress = lambda: b"\0"
with open("test_xz_bad_1.xz", "rb") as f:
    data = f.read()

decomp.decompress(data)
# Patch LZMADecompressor to return nothing
decomp.decompress = lambda: b""
with open("test_xz_bad_1.xz", "rb") as f:
    data = f.read()

decomp.decompress(data)
# Patch LZMADecompressor to return some data
decomp.decompress = lambda: b"\0"
with open("test_xz_bad_2.xz", "rb") as f:
    data = f.read()

decomp
