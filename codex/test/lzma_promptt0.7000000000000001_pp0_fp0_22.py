import lzma
# Test LZMADecompressor.

decompressor = lzma.LZMADecompressor()

decompressor.decompress(b"\x00")

# EOFError
decompressor.decompress(b"\x00")

# Test LZMADecompressor.decompress()
# Test an empty input.
decompressor.decompress(b"")

# Test a small input.
decompressor.decompress(b"\x00")

# Test a large input.
decompressor.decompress(b"\x00" * 1000)

# Test a large input in multiple steps.
data = b"\x00" * 1000
