import lzma
# Test LZMADecompressor
compressor = lzma.LZMADecompressor()
compressor.decompress(b"\x00\x00")
# Test LZMACompressor
compressor = lzma.LZMACompressor()
compressor.compress(b"\x00\x00")
compressor.flush()

# Test LZMAFile
f = lzma.LZMAFile(BytesIO())
f.close()
f = lzma.LZMAFile(BytesIO(), mode="w")
f.close()
f = lzma.LZMAFile(BytesIO(), mode="w", format=lzma.FORMAT_XZ)
f.close()
f = lzma.LZMAFile(BytesIO(), mode="w", check=lzma.CHECK_CRC64)
f.close()
f = lzma.LZMAFile(BytesIO(), mode="w", preset=9)
f.close()
f = lzma.LZMAFile(BytesIO(), mode="w", filters=[])
f.close()
