import bz2
# Test BZ2Decompressor
bz_dec = bz2.BZ2Decompressor()
line = next(data)
# Test that the initial decompression of first line works
# without the need to call decompressor.decompress() first
result = bz_dec.decompress(line)
print(result)

# Test BZ2Decompressor.decompress()
resul
