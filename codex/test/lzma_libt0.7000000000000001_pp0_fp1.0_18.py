import lzma
lzma.LZMACompressor()

print(lzma.LZMAError)

x = lzma.LZMADecompressor()
x.unused_data
x.eof

x.decompress(b"")
x.unused_data
x.eof

