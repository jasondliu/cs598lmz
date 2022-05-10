import lzma
lzma.LZMACompressor()

print(lzma.LZMAError)

x = lzma.LZMADecompressor()
x.unused_data
x.eof

x.decompress(b"")
x.unused_data
x.eof

x.decompress(b"a")
x.unused_data
x.eof

x.decompress(b"a")
print(x.unused_data)
x.eof

x.decompress(b"")
print(x.unused_data)
x.eof

x.decompress(b"")
print(x.unused_data)
x.eof

x.decompress(b"")
print(x.unused_data)
x.eof

# b"" -> b"a" -> b"" -> b"" -> b"" -> b"a" -> b""
#                                   ^
#                                   |
#                                   +-- EOF here

print(x.decomp
