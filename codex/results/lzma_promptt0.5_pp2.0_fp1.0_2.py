import lzma
# Test LZMADecompressor with a small input buffer.
# See https://bugs.python.org/issue33185
with lzma.LZMADecompressor() as decompressor:
    decompressor.decompress(b"\x00" * 9)
    decompressor.decompress(b"\x00" * 9)
    decompressor.decompress(b"\x00" * 9)
    decompressor.decompress(b"\x00" * 9)
    decompressor.decompress(b"\x00" * 9)
    decompressor.decompress(b"\x00" * 9)
    decompressor.decompress(b"\x00" * 9)
    decompressor.decompress(b"\x00" * 9)
    decompressor.decompress(b"\x00" * 9)
    decompressor.decompress(b"\x00" * 9)
    decompressor.decompress(b"\x00" * 9)
    decompressor.decompress(b"\x00" * 9)
   
