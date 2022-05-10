import lzma
# Test LZMADecompressor:
dec = lzma.LZMADecompressor()
output = dec.decompress(data)
print("After decompression:  ", len(output))
