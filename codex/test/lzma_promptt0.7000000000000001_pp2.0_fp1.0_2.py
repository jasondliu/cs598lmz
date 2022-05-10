import lzma
# Test LZMADecompressor.eof property
d = lzma.LZMADecompressor()
d.decompress(b"")
d.eof
d.decompress(b"\x00")
d.eof
d.decompress(b"\x00")
d.eof
d.decompress(b"")
d.eof
d.decompress(b"")
d.eof
d.decompress(b"")
d.eof
# Test LZMADecompressor.decompress() with partial input
d = lzma.LZMADecompressor()
for i in range(5):
    d.decompress(b"\x00")
    d.eof
d.decompress(b"\x00")
d.eof
d.decompress(b"")
d.eof
d.decompress(b"")
d.eof
d.decompress(b"")
d.eof
