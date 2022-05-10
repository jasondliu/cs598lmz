import lzma
# Test LZMADecompressor
dec = lzma.LZMADecompressor()
data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00'
dec.decompress(data)

# Test LZMAFile
