import lzma
lzma.LZMADecompressor().decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00')

lzma.LZMADecompressor().decompress(b'\x01\x00\x00\x00\x00\x00\x00\x00')

lzma.LZMADecompressor().decompress(b'\x01\x01\x00\x00\x00\x00\x00\x00')

lzma.LZMADecompressor().decompress(b'\x01\x01\x01\x00\x00\x00\x00\x00')

lzma.LZMADecompressor().decompress(b'\x01\x01\x01\x01\x00\x00\x00\x00')

lzma.LZMADecompressor().decompress(b'\x01\x01\x01\x01\x
