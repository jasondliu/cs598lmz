import lzma
lzma.decompress(b"\x00").decode()

xz.decompress(b"\x00").decode()

# lzma.LZMADecompressor().decompress(b"\x00").decode()
# xz.LZMADecompressor().decompress(b"\x00").decode()
# xz.LZMADecompressor(lzma.FORMAT_AUTO).decompress(b"\x00").decode()

# lzma.LZMADecompressor(format=-1).decompress(b"\x00").decode()
# lzma.LZMADecompressor(format=10).decompress(b"\x00").decode()
