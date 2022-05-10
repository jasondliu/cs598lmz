import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
decomp.decompress(b"Test")

try:
    decomp.decompress(b"Test")
except RuntimeError:
    pass
else:
    print("Failed to raise error on second decompress() call")

try:
    decomp.decompress(b"\x7f")
except ValueError:
    pass
else:
    print("Failed to raise error when not enough data")

decomp.decompress(b"\x7f""\x80""data")

assert decomp.unused_data == b"data"
# Test decompress() with a certain amount of input data
decomp = lzma.LZMADecompressor()
decomp.decompress(b"\x7f""\x80""data", 1)
decomp.decompress(b"\x7f""\x80""data", 2)
decomp.decompress(b"\x7f""\x80""data", 3)

assert decomp.unused
